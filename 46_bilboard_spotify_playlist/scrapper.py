import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard-japan.com/charts/detail"

class Scrapper():
    
    def __init__(self,  year: int) -> None:
        self.year = year

    def get_year_songs(self):
        """
        Go to Billboard hot 100 and scrape the top 100 songs of the given year.

        Returns:
            dict: a dictionary with {song: artist} format.
        """
        params = {
            "a": "hot100_year",
            "year": self.year,
        }

        r = requests.get(URL, params=params)
        r.raise_for_status()
        
        soup = BeautifulSoup(r.text, "html.parser")
        songs = [song.getText().strip() for song in soup.find_all("p", class_="musuc_title")]

        artists = []
        for p in soup.find_all("p", class_="artist_name"):
            artist = p.find("a")
            if artist:
                artists.append(artist.getText())
            else:
                # some artists does not have a dedicated artist page/hiperlink
                artists.append(p.getText())

        songs_artists = dict(zip(songs, artists))
        return songs_artists