import requests
import os
import spotipy
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import plotly.express as go


# Test  1: status_code is 200; if everything is correct
# Test  2: status_code is not 200; if the AUTH_URL is incorrect
# Test  3: status_code is not 200; if CLIENT_ID is incorrect
# Test  4: status_code is not 200; if CLIENT_SECRET is incorrect
def getAuthresponse(AUTH_URL, CLIENT_ID, CLIENT_SECRET):
    auth_response = requests.post(AUTH_URL, {
      'grant_type': 'client_credentials',
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET,
    })
    return auth_response


def getAccessToken(AUTH_URL, CLIENT_ID, CLIENT_SECRET):
    auth_response = getAuthresponse(AUTH_URL, CLIENT_ID, CLIENT_SECRET)
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    return access_token


def getHeader(AUTH_URL, CLIENT_ID, CLIENT_SECRET):
    access_token = getAccessToken(AUTH_URL, CLIENT_ID, CLIENT_SECRET)
    headers = {
      'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    return headers


# Test  1: check if artist_id is not vaild
# Test  2: check if base url is vaild
# Test  3: check if json worked
def convertToJson(BASE_URL, artist_id, AUTH_URL, CLIENT_ID, CLIENT_SECRET):
    headers = getHeader(AUTH_URL, CLIENT_ID, CLIENT_SECRET)
    r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums',
                     headers=headers, params={'limit': 10})
    return r.json()


def displayTitle(title):
    print(title)
    print('-' * len(title))


def displayAlbum(title, response):
    displayTitle(title)
    for info in response['items']:
        print(info['name'] + ' was released on ' + info['release_date']
              + " with " + str(info['total_tracks']) + ' total tracks.')


# Test  1: check if artist_id is not vaild
# Test  2: check if base url is vaild
# Test  2: check if json worked
def convertToJsonT(BASE_URL, artist_id, AUTH_URL, CLIENT_ID, CLIENT_SECRET):
    headers = getHeader(AUTH_URL, CLIENT_ID, CLIENT_SECRET)
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
    return df


def createEngine(database_name):
    engine = create_engine('mysql://root:codio@localhost/'
                           + database_name + '?charset=utf8', encoding='utf-8')
    return engine


def createTable(database_name, top_tracks, table_name):
    df = convertToDataFrame(top_tracks)
    engine = createEngine(database_name)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)


def pie(dataframe):
    fig = go.sunburst(dataframe, path = ['Popularity','Track_Name'],
                      values = 'Popularity',
                      color= 'Track_Name',
                      title = 'Percentage of the Popularity of Doja Top 10 Tracks')
    fig.write_html('hist.html')


def saveSQLtoFile(database_name, file_name):
    os.system('mysqldump -u root -pcodio ' + database_name + ' > ' + file_name)


def loadSQLfromFile(database_name, file_name):
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + database_name + ';"')
    os.system('mysql -u root -pcodio ' + database_name + ' < ' + file_name)


def loadDataset(database_name, table_name, file_name, update=False):
    loadSQLfromFile(database_name, file_name)
    df = pd.read_sql_table(table_name, con=createEngine(database_name))
    if update:
        return loadNewData(df)
    else:
        return df


# assigning variables

CLIENT_ID = '7bb5a610971f437690b91981206e0025'
CLIENT_SECRET = 'f102316e6e7b45bd93e1988be3162cf6'
AUTH_URL = 'https://accounts.spotify.com/api/token'
table_name = 'Top_Tracks'
artist_id = '5cj0lLjcoR7YOSnhnX0Po5'
BASE_URL = 'https://api.spotify.com/v1/'
title = "Doja Cat's last Ten Released Albums"
ntitle = 'Top Tracks in the US'
database_name = 'spotifydoja'


tracks = convertToJsonT(BASE_URL, artist_id, AUTH_URL, CLIENT_ID,
                        CLIENT_SECRET)
response = convertToJson(BASE_URL, artist_id, AUTH_URL, CLIENT_ID,
                         CLIENT_SECRET)
file_name = 'spotifydata.sql'
displayAlbum(title, response)
top_tracks = displayTopTracks(ntitle, tracks)
dataframe = convertToDataFrame(top_tracks)
createTable(database_name, top_tracks, table_name)
df = loadDataset(database_name, table_name, file_name)
pie(df)
