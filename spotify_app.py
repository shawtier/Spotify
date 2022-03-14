
import streamlit as st
from spotipy_client import *

client_id = 'your_client_id'
client_secret = 'your_client_secret'

spotify = SpotifyAPI(client_id, client_secret)








Data = spotify.search({"artist": f"{Name_of_Artist}"}, search_type="track")

 
Track_df = pd.DataFrame(need, index=None, columns=('Item', 'Artist', 'Album Name', 'Id', 'Song Name', 'Release Date', 'Popularity'))

access_token = spotify.access_token

headers = {
    "Authorization": f"Bearer {access_token}"
}
endpoint = "https://api.spotify.com/v1/audio-features/"



Full_Data = Track_df.merge(Feat_df, left_on="Id", right_on="id")

Sort_DF = Full_Data.sort_values(by=['Popularity'], ascending=False)

chart_df = Sort_DF[['Artist', 'Album Name', 'Song Name', 'Release Date', 'Popularity', f'{Name_of_Feat}']]



def data_time_range(timespan):
    if (timespan == '1 Month'):
        return 'short_term'
    elif (timespan == '6 Months'):
        return 'medium_term'
    elif (timespan =='All Time'):
        return 'long_term'

timeframe= st.radio(
     "Pick a time frame",
     ('1 Month', '6 Months', 'All Time')
)

data=sp.current_user_top_tracks(limit=10, offset=1, time_range= data_time_range(timeframe))

ids=get_track_ids(data)



for id in ids:
    st.write(f"{get_track_features(id)[0]} by {get_track_features(id)[2]}")


