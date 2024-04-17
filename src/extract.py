import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv('env')

def extract():
    cred = SpotifyClientCredentials(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    )

    sp = spotipy.Spotify(client_credentials_manager=cred)

    data = sp.playlist_tracks(os.getenv("PLAYLIST_ID"))

    #print(data)
    return data