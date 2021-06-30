import requests
import spotipy
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

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
title = "Doja Cat's last Ten Released Albums"


# Test  1: check if artist_id is not vaild
# Test  2: check if base url is vaild
# Test  2: check if json worked
def convertToJson(BASE_URL, artist_id):
    r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums',
                     headers=headers, params={'limit': 10})
    return r.json()


# Test  1: Check if display looks like its supposed to
def displayTitle(title):
    print(title)
    print('-' * len(title))


# Test  1: check if the title is displayed correctly
# Test  2: check if response is in correct format
# Test  2: check if print is printed correctly
def displayAlbum(title, response):
    displayTitle(title)
    for info in response['items']:
        print(info['name'] + ' was released on ' + info['release_date']
              + " with " + str(info['total_tracks']) + ' total tracks.')


# Test  1: check if artist_id is not vaild
# Test  2: check if base url is vaild
# Test  2: check if json worked
def convertToJsonTrack(BASE_URL, artist_id):
    track = requests.get(BASE_URL + 'artists/' + artist_id
                        + '/top-tracks?market=us', headers=headers)
    return track.json()


# Test  1: check if the title is displayed correctly
# Test  2: check if response is in correct format
# Test  2: check if print is printed correctly
def displayTopTracks(title, tracks):
    displayTitle(title)
    top_tracks = {}
    i = 0
    for t in tracks['tracks']:
        top_tracks[i] = [t['name'], t['explicit'], t['popularity']]
        i += 1
        if t['explicit']:
            print(t['name'] + ' which has a popularity of '
                  + str(t['popularity']) + ' and is explicit.')
        else:
            print(t['name'] + ' which has a popularity of '
                  + str(t['popularity']))
    return top_tracks


# Test  1: display correct info
def convertToDataFrame(top_tracks):
    df = pd.DataFrame.from_dict(top_tracks, orient='index', columns=[
      'Track_Name', 'Explicit', 'Popularity'])
    engine = create_engine('mysql://root:codio@localhost/spotifydoja')
    df.to_sql('Top_Tracks', con=engine, if_exists='replace', index=False)


response = convertToJson(BASE_URL, artist_id)
displayAlbum(title, response)
tracks = convertToJsonTrack(BASE_URL, artist_id)
ntitle = 'Top Tracks in the US'
top_tracks = displayTopTracks(ntitle, tracks)
convertToDataFrame(top_tracks)
