from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Playlist():
    def __init__(self) -> None:
        load_dotenv()
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
                scope="playlist-modify-private",
                redirect_uri="https://example.org/callback",
                show_dialog=True,
                cache_path="token.txt",
                username=os.getenv("SPOTIFY_USERNAME")
            )
        )
        self.user_id = self.sp.current_user()["id"]

    def generate_uris(self, songs_artists: dict, year: int) -> list:
        """
        Using Spotify API search for songs/artist pair in each element of the dictionary
        and returns a list of Spotify uris.

        Args:
            songs_artists (dict): a dictionary in the {song: artist} format.
            year (int): year of the songs in the dictionary, helps with search query. 

        Returns:
            list: a list of uris that are the result of the search of each song.
        """
        result_uris = []
        for song, artist in songs_artists.items():
            query = f"track: {song} artist: {artist} year: {year}"
            result = self.sp.search(q=query, type="track", market="JP", limit=1)
            result_uris.append(result["tracks"]["items"][0]["uri"])

        return result_uris
    
    def create_playlist(self, year: int) -> str:
        """
        Using Spotify API create a playlist.

        Args:
            year (int): year of the top 100 playlist used in the playlist title.

        Returns:
            str: newly generated playlist id.
        """
        playlist_name = f"{year} Bilboard Japan 100"
        playlst = self.sp.user_playlist_create(user=self.user_id, name=playlist_name, public=False)
        return playlst["id"]

    def add_to_playlist(self, playlist_id: str, uris: list) -> None:
        """
        Add all the uris (tracks) to the playlist.

        Args:
            playlist_id (str): id of the playlist to add tracks
            uris (list): a list of Spotify uris (tracks)
        """
        self.sp.playlist_add_items(playlist_id, uris)
        print("Playlist generated, check your Spotify account")
