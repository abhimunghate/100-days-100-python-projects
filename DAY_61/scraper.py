# Day 61 - Social Media Scraper
# Scraping Module

from bs4 import BeautifulSoup

def load_html(file_path):
    """Load HTML content from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def extract_posts(html_content):
    """Extract social media post information from HTML."""
    soup = BeautifulSoup(html_content, "html.parser")
    posts = []
    post_elements = soup.find_all("div", class_="post")

    for post in post_elements:
        post_id = post.get("id", "Unknown")
        username_element = post.find("h2", class_="username")
        username = (username_element.get_text(strip=True) if username_element else "Unknown")
        content_element = post.find("p", class_="content")
        content = (content_element.get_text(" ", strip=True) if content_element else "")
        timestamp_element = post.find("span", class_="timestamp")
        timestamp = (timestamp_element.get_text(strip=True) if timestamp_element else "Unknown")
        likes_element = post.find("span", class_="likes")
        likes_text = (likes_element.get_text(strip=True) if likes_element else "0")
        
        try:
            likes = int(likes_text)
        except ValueError:
            likes = 0

        posts.append({"post_id": post_id, "username": username, "content": content, "timestamp": timestamp, "likes": likes})
    return posts

# Done