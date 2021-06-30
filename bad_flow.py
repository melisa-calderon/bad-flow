from sqlalchemy import create_engine
import requests
import spotipy
import pandas as pd
import sqlalchemy 


CLIENT_ID = '7bb5a610971f437690b91981206e0025'
CLIENT_SECRET = 'f102316e6e7b45bd93e1988be3162cf6'

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
  'grant_type': 'client_credentials',
  'client_id': CLIENT_ID,
  'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']

headers = {
  'Authorization': 'Bearer {token}'.format(token=access_token)
}
artist_id = '5cj0lLjcoR7YOSnhnX0Po5'
BASE_URL = 'https://api.spotify.com/v1/'
r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums',
                 headers=headers, params={'limit': 10})
response = r.json()
title = "Doja Cat's last Ten Released Albums"
print(title)
print('-' * len(title))
for info in response['items']:
    print(info['name'] + ' was released on ' + info['release_date']
          + " with " + str(info['total_tracks']) + ' total tracks.')

track = requests.get(BASE_URL + 'artists/' + artist_id
                     + '/top-tracks?market=us', headers=headers)
tracks = track.json()
ntitle = 'Top Tracks in the US'
print(ntitle)
print('-' * len(ntitle))
top_tracks = {}
i =0
for t in tracks['tracks']:
    top_tracks[i] = [t['name'], t['explicit'], t['popularity']]
    i += 1
    if t['explicit']:
        print(t['name'] + ' which has a popularity of ' + str(t['popularity'])
              + ' and is explicit.')
    else:
        print(t['name'] + ' which has a popularity of ' + str(t['popularity']))

df = pd.DataFrame.from_dict(top_tracks, orient = 'index', columns=['Track_Name', 'Explicit', 'Popularity'])

engine = create_engine('mysql://root:codio@localhost/spotifydoja')
df.to_sql('Top_Tracks', con=engine, if_exists='replace', index=False)
