import requests

class Post:
    def __init__(self) -> None:
        api = "https://api.npoint.io/19178aee7e641ba9e7fc"
        self.r = requests.get(api)
        self.r.raise_for_status()

    def get_all_posts(self):
        return self.r.json()