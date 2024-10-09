from scrapper import Scrapper
from playlist import Playlist

year = int(input("Which year you want to travel to? Type the year in this format YYYY: "))

scrapper = Scrapper(year)
songs_artists = scrapper.get_year_songs()

playlist = Playlist()
uris = playlist.generate_uris(songs_artists, year)
id = playlist.create_playlist(year)
playlist.add_to_playlist(id, uris)