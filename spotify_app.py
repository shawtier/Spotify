
import requests
from spotipy_client import *
import pandas as pd
import streamlit as st

SPOTIFY_CLIENT_ID = 'your_client_id'
SPOTIFY_CLIENT_SECRET = 'your_client_secret'

spotify = SpotifyAPI(client_id, client_secret)


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
