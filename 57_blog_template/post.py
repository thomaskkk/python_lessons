import requests

class Post:
    def __init__(self) -> None:
        api = "https://api.npoint.io/c790b4d5cab58020d391"
        self.r = requests.get(api)
        self.r.raise_for_status()

    def get_all_posts(self):
        return self.r.json()