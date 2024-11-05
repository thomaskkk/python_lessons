import requests
from datetime import datetime

class Post():
    """docstring for Post."""
    def __init__(self):
        posts_url = "https://api.npoint.io/ae161abade368170392a"
        self.r = requests.get(posts_url)
        self.r.raise_for_status()

    def get_posts(self):
        self.blog_posts = []
        for item in self.r.json():
            item["date"] = datetime.strptime(item["date"], "%Y-%m-%d").strftime("%B %d, %Y")
            self.blog_posts.append(item)
        return self.blog_posts
    