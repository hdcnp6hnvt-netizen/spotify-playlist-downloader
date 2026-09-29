import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

REDIRECT_URI = "http://127.0.0.1:8888/callback"

if not CLIENT_ID or not CLIENT_SECRET:
    print("Errore: mancano le credenziali Spotify.")
    print("Imposta SPOTIFY_CLIENT_ID e SPOTIFY_CLIENT_SECRET.")
    exit()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-read-private"
    )
)

playlist_url = input("Incolla il link della playlist Spotify: ")

playlist = sp.playlist(playlist_url)

print()
print("Playlist:", playlist["name"])
print("-" * 50)

for item in playlist["tracks"]["items"]:
    track = item.get("track")

    if track:
        artists = ", ".join(
            artist["name"]
            for artist in track["artists"]
        )

        print(f"{track['name']} - {artists}")
