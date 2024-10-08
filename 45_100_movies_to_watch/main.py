import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

r = requests.get(URL)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")
movie_titles = [movie.getText() for movie in soup.find_all("h3", class_="title")]
movie_titles.reverse()

with open("movies.txt", mode="w") as data:
    for movie in movie_titles:
        data.write(f"{movie}\n")