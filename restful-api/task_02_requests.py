import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """Fetch posts and print the status code + titles."""
    response = requests.get(API_URL)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If successful, parse JSON
    if response.status_code == 200:
        posts = response.json()

        # Print each post title
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """Fetch posts and save selected fields to posts.csv."""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()

        # Create list of dictionaries with id, title, body
        formatted_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(formatted_posts)

        print("posts.csv created successfully.")
    else:
        print("Failed to fetch and save posts.")