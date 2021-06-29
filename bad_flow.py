import requests
import spotipy

CLIENT_ID ='7bb5a610971f437690b91981206e0025'
CLIENT_SECRET = 'f102316e6e7b45bd93e1988be3162cf6'

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL,{
  'grant_type': 'client_credentials',
  'client_id': CLIENT_ID,
  'client_secret':CLIENT_SECRET,
})
print(auth_response.status_code)