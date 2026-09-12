# Day 63 - Movie Recommendation System
# Item-based collaborative filtering with genre similarity

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def load_ratings(file_path):
    """Loads the movie ratings CSV file."""
    return pd.read_csv(file_path)

def load_genres(file_path):
    """Loads the movie genres CSV file."""
    return pd.read_csv(file_path)

def prepare_ratings_matrix(ratings):
    """Creates a movie-user matrix.
    Rows    = movies
    Columns = users
    Values  = ratings
    """
    ratings_matrix = ratings.pivot_table(index="movie", columns="user", values="rating", aggfunc="mean").fillna(0)
    return ratings_matrix

def prepare_genre_matrix(genres):
    """Converts movie genres into a binary genre matrix."""
    genre_matrix = genres.copy()
    genre_matrix["genres"] = genre_matrix["genres"].fillna("")
    genre_matrix = genre_matrix.assign(genres=genre_matrix["genres"].str.split("|"))
    genre_matrix = genre_matrix.explode("genres")
    genre_matrix["value"] = 1
    genre_matrix = genre_matrix.pivot_table(index="movie", columns="genres", values="value", aggfunc="max", fill_value=0)
    return genre_matrix

def calculate_item_similarity(ratings_matrix):
    """Calculates similarity between movies based on user ratings."""
    similarity = cosine_similarity(ratings_matrix)
    return pd.DataFrame(similarity, index=ratings_matrix.index, columns=ratings_matrix.index)

def calculate_genre_similarity(genre_matrix):
    """Calculates similarity between movies based on genres."""
    similarity = cosine_similarity(genre_matrix)
    return pd.DataFrame(similarity, index=genre_matrix.index, columns=genre_matrix.index)

def get_user_rated_movies(user_id, ratings_matrix):
    """Returns movies already rated by the selected user."""
    if user_id not in ratings_matrix.columns:
        return []

    user_ratings = ratings_matrix[user_id]
    rated_movies = user_ratings[user_ratings > 0]
    return rated_movies

def recommend_movies(user_id, ratings_matrix, rating_similarity, genre_similarity, rating_weight=0.7, genre_weight=0.3, recommendation_count=5):
    """Recommends movies using item-based collaborative filtering.

    Rating similarity and genre similarity are combined into one recommendation score."""
    if user_id not in ratings_matrix.columns:
        return []

    user_rated_movies = get_user_rated_movies(user_id, ratings_matrix)
    if user_rated_movies.empty:
        return []
    recommendations = {}

    for rated_movie, user_rating in user_rated_movies.items():
        similar_movies = rating_similarity[rated_movie].sort_values(ascending=False)

        for candidate_movie, rating_score in similar_movies.items():
            if candidate_movie in user_rated_movies.index:
                continue

            genre_score = 0

            if (rated_movie in genre_similarity.index and candidate_movie in genre_similarity.columns):
                genre_score = genre_similarity.loc[rated_movie, candidate_movie]

            combined_score = ((rating_score * rating_weight) + (genre_score * genre_weight)) * user_rating
            if candidate_movie not in recommendations:
                recommendations[candidate_movie] = combined_score
            else:
                recommendations[candidate_movie] += combined_score

    sorted_recommendations = sorted(recommendations.items(), key=lambda item: item[1], reverse=True)
    return sorted_recommendations[:recommendation_count]

def get_movie_genres(movie_name, genres):
    """Returns the genres of a movie."""
    matching_movie = genres[genres["movie"] == movie_name]
    if matching_movie.empty:
        return "Unknown"
    return matching_movie.iloc[0]["genres"].replace("|", ", ")

def build_recommendation_data(user_id, ratings_matrix, rating_similarity, genre_similarity, genres, recommendation_count=5):
    """Creates formatted recommendation results for the GUI."""
    recommendations = recommend_movies(user_id=user_id, ratings_matrix=ratings_matrix, rating_similarity=rating_similarity, genre_similarity=genre_similarity, recommendation_count=recommendation_count)
    result = []

    for movie, score in recommendations:
        result.append({"movie": movie, "genres": get_movie_genres(movie, genres), "score": round(score, 3)})
    return result

# Done