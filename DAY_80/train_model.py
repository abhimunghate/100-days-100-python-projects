# This is Day 80 project : Fake News Detector
# Model Training - TF-IDF + Random Forest

import os
import re
import joblib
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix)
from sklearn.model_selection import train_test_split

FAKE_PATH = "dataset/Fake.csv"
REAL_PATH = "dataset/True.csv"

MODEL_DIR = "models"

MODEL_PATH = os.path.join(MODEL_DIR, "fake_news_model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")
RANDOM_STATE = 42

print("Checking NLTK resources...")
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

try:
    nltk.download("punkt_tab", quiet=True)
except Exception:
    pass

stop_words = set(stopwords.words("english"))

def clean_text(text):
    """Clean and normalize news article text."""
    if pd.isna(text):
        return ""

    text = str(text).lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words and len(word) > 2]
    return " ".join(tokens)

def load_dataset():
    print("\nLoading dataset...")
    if not os.path.exists(FAKE_PATH):
        raise FileNotFoundError(f"Fake dataset not found: {FAKE_PATH}")

    if not os.path.exists(REAL_PATH):
        raise FileNotFoundError(f"Real dataset not found: {REAL_PATH}")

    fake_df = pd.read_csv(FAKE_PATH)
    real_df = pd.read_csv(REAL_PATH)
    print(f"Fake articles : {len(fake_df)}")
    print(f"Real articles : {len(real_df)}")

    fake_df["label"] = 0
    real_df["label"] = 1

    df = pd.concat([fake_df, real_df], ignore_index=True)
    df = df.dropna(subset=["text"])

    if "title" in df.columns:
        df["combined_text"] = (df["title"].fillna("") + " " + df["text"].fillna(""))
    else:
        df["combined_text"] = (df["text"].fillna(""))

    df = df.sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)
    return df

def train_model():
    print("=" * 60)
    print("DAY 80 - FAKE NEWS DETECTOR")
    print("TF-IDF + RANDOM FOREST")
    print("=" * 60)

    os.makedirs(MODEL_DIR, exist_ok=True)

    df = load_dataset()
    print(f"\nTotal articles: {len(df)}")
    print("\nCleaning text...")

    df["cleaned_text"] = df["combined_text"].apply(clean_text)
    df = df[df["cleaned_text"].str.strip() != ""]
    print(f"Articles after cleaning: {len(df)}")

    print("\nCreating TF-IDF features...")
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2), min_df=2, max_df=0.95, sublinear_tf=True)
    X = vectorizer.fit_transform(df["cleaned_text"])
    y = df["label"]

    print(f"TF-IDF feature shape: {X.shape}")

    print("\nSplitting dataset...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=RANDOM_STATE, stratify=y)

    print(f"Training samples: {X_train.shape[0]}")
    print(f"Testing samples : {X_test.shape[0]}")

    print("\nTraining Random Forest...")
    model = RandomForestClassifier( n_estimators=150, max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features="sqrt", class_weight="balanced", random_state=RANDOM_STATE, n_jobs=-1)
    model.fit( X_train, y_train)
    print("Training completed.")

    print("\nEvaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("\n" + "=" * 60)
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print("=" * 60)
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=["FAKE", "REAL"]))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nSaving model...")
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    print(f"Model saved to: {MODEL_PATH}")
    print(f"Vectorizer saved to: {VECTORIZER_PATH}")
    print("\nTraining completed successfully!")

if __name__ == "__main__":
    train_model()
    
# Done