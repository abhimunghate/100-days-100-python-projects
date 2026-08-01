# This is Day 21 project : Wikipedia Article Scraper

import requests
from bs4 import BeautifulSoup
import json
import os

TEXT_FILE = "wikipedia_articles.txt"
JSON_FILE = "wikipedia_articles.json"

if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump([], file, indent=4)
        
def load_articles():
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_to_json(title, summary, headings, related_links):
    articles = load_articles()
    
    for article in articles:
        if article["Title"].lower() == title.lower():
            print("\nThis article already exists in the JSON file.")
            return

    articles.append({"Title": title, "Summary": summary, "Headings": headings[:5], "Related Links": related_links})
    save_articles(articles)

    print("\nArticle exported to JSON successfully.")

def save_articles(articles):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(articles, file, indent=4, ensure_ascii=False)

headers = {"User-Agent": "Mozilla/5.0"}

def get_wikipedia_page(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        elif response.status_code == 404:
            print("Article not found.")
        else:
            print(f"Failed to retrieve data. Status code : {response.status_code}.")
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"Network Error : {e}")
        return None
    
def get_article_title(soup):
    title = soup.find('h1')
    return title.text if title else "No Title Found"

def get_article_summary(soup):
    paragraphs = soup.find_all('p')
    for para in paragraphs:
        if para.text.strip():
            return para.text.strip()
    return "No summary found"
    
def get_headings(soup):
    headings = [heading.text.strip() for heading in soup.find_all(['h2', 'h3', 'h4'])]
    return headings

def get_related_links(soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/wiki/') and ":" not in href:
            links.append(f"https://en.wikipedia.org{href}")
    return list(dict.fromkeys(links))[:5]

def save_to_text(title, summary, headings, related_links):
    with open(TEXT_FILE, "a", encoding="utf-8") as file:
        file.write("=" * 60 + "\n")
        file.write(f"Article: {title}\n")
        file.write("=" * 60 + "\n\n")

        file.write("Summary:\n")
        file.write(summary + "\n\n")

        file.write("Headings:\n")
        for i, heading in enumerate(headings[:5], start=1):
            file.write(f"{i}. {heading}\n")

        file.write("\nRelated Links:\n")
        for link in related_links:
            file.write(f"- {link}\n")

        file.write("\n\n")

    print("\nArticle saved successfully.")
    
def save_menu():
    print("\n------ Save Options ------")
    print("1. Save as Text File")
    print("2. Export to JSON")
    print("3. Save Both")
    print("4. Don't Save")

    return input("\nEnter your choice (1-4): ").strip()
    
def main():
    while True:
        topic = input("\nEnter a topic to search on Wikipedia (or 'q' to quit) : ").strip()
        
        if topic.lower() == "q":
            print("\nThank you for using Wikipedia Article Scraper.")
            break

        if not topic:
            print("Topic cannot be empty.")
            continue
        
        page_content = get_wikipedia_page(topic)
        
        if page_content:
            soup = BeautifulSoup(page_content, 'html.parser')
            title = get_article_title(soup)
            summary = get_article_summary(soup)
            headings = get_headings(soup)
            related_links = get_related_links(soup)
            
            print("\n------ Wikipedia Article Details ------")
            print(f"\nTitle : {title}")
            if len(summary) > 500:
                print(f"\nSummary : {summary[:500]}...")
            else:
                print(f"\nSummary : {summary}")
            print(f"\nHeadings :")
            for i, heading in enumerate(headings[:5], start=1):
                print(f"{i}. {heading}")
                
            print("\nRelated Links : ")
            for link in related_links:
                print(f"- {link}")
                
            choice = save_menu()

            if choice == "1":
                save_to_text(title, summary, headings, related_links)

            elif choice == "2":
                save_to_json(title, summary, headings, related_links)

            elif choice == "3":
                save_to_text(title, summary, headings, related_links)
                save_to_json(title, summary, headings, related_links)

            elif choice == "4":
                print("\nArticle not saved.")

            else:
                print("\nInvalid choice. Article not saved.")
            
if __name__ == "__main__":
    main()
    
# Done