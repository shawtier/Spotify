sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import streamlit as st



SPOTIPY_CLIENT_ID="c848c34a824f4a638ea4d5852db0e645"
SPOTIPY_CLIENT_SECRET="221e2c2c77844e0e871f913c68877275"
SPOTIPY_REDIRECT_URI="http://127.0.0.1:9090"
SCOPE = "user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))
st.write('Spotify Stats')

timeframe= st.radio(
     "Pick a time frame",
     ('Last Month', 'Last Year', 'All Time')
)

if (timeframe == 'Last Month'):
     data=sp.current_user_top_tracks(limit=10,time_range='short_term')
elif (timeframe == 'Last Year'):
     data=sp.current_user_top_tracks(limit=10, time_range='medium_term')
else :
     data=sp.current_user_top_tracks(limit=10,time_range='long_term')

def get_track_ids(time_frame):
    track_ids = []
    for song in time_frame["items"]:
        track_ids.append(song["id"])
    return track_ids
ids=get_track_ids(data)


def get_track_features(id):
    meta = sp.track(id)
    # meta
    name = meta["name"]
    preview_url = meta["preview_url"]
    album = meta["album"]["name"]
    artist = meta["album"]["artists"][0]["name"]
    spotify_url = meta["external_urls"]["spotify"]
    album_cover = meta["album"]["images"][0]["url"]
    track_info = [name, album, artist, spotify_url, album_cover, preview_url]
    return track_info


topSongsList = []

for id in ids:
    topSongsList.append(f"{get_track_features(id)[0]} by {get_track_features(id)[2]}")

st.write(topSongsList)
