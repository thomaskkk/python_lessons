import requests
from datetime import datetime

class Post():
    """docstring for Post."""
    def __init__(self):
        posts_url = "https://api.npoint.io/ae161abade368170392a"
        r = requests.get(posts_url)
        r.raise_for_status()
        self.blog_posts = []
        for item in r.json():
            item["date"] = datetime.strptime(item["date"], "%Y-%m-%d").strftime("%B %d, %Y")
            self.blog_posts.append(item)

    def get_posts(self):

        return self.blog_posts
    
    def get_single_post(self, post_num):
        for item in self.blog_posts:
            if item["id"] == post_num:
                return item