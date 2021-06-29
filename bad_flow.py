import requests
import spotipy

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

print("Doja Cat's last Ten Released Albums")
print("-----------------------------------")
for info in response['items']:
        print(info['name']+' was released on '+info['release_date'] + 
              " with " + str(info['total_tracks']) + ' total tracks.')