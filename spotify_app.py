
import streamlit as st
from spotipy_client import *

client_id = 'your_client_id'
client_secret = 'your_client_secret'

spotify = SpotifyAPI(client_id, client_secret)

Name_of_Artist = st.text_input("Artist Name")

data = spotify.search({"artist": f"{Name_of_Artist}"}, search_type="track")

access_token = spotify.access_token

headers = {
    "Authorization": f"Bearer {access_token}"
}
endpoint = "https://api.spotify.com/v1/audio-features/"

need=[]
for i, item in enumerate(data['tracks']['items']):
    track = item['album']
    track_id = item['id']
    song_name = item['name']
    popularity = item['popularity']
    need.append((i, track['artists'][0]['name'], track['name'], track_id, song_name, track['release_date'], popularity))
    


st.write(need)


