# Bilboard Spotify Playlist

This is an program that scrape top 100 Bilboard and create a playlist in Spotify.


This challenge teaches the concepts of:

 - BeautifulSoup web scraping
 - HTTP API requests
 - HTTP Auth (oauth2)

## Setup

This program uses the Python requests, bs4, pyhton-dotenv and spotipy

```
pip install -r requirements.txt
```
or

```
pip install requests bs4 python-dotenv spotipy
```
With your Spotify account go to [developer dashboard](https://developer.spotify.com/dashboard/) and create a new Spotify App.

Use `https://example.org/callback` as your Redirect URIs.

Rename .env_sample to .env and fill with your credentials from Spotify App.

## How to run

```
python main.py
```

At the first time running you should see a link in the console, open it, allow the oauth2 access, and copy the whole url that you will be redirected and paste back in the console, that will generate a file "token.txt".