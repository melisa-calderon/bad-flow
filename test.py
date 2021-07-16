import unittest
from bad_flow import getAuthresponse, convertToJson, convertToJsonT

BASE_URL = 'https://api.spotify.com/v1/'
AUTH_URL = 'https://accounts.spotify.com/api/token'
CLIENT_ID = '7bb5a610971f437690b91981206e0025'
CLIENT_SECRET = 'f102316e6e7b45bd93e1988be3162cf6'
artist_id = '5cj0lLjcoR7YOSnhnX0Po5'

class TestFileName(unittest.TestCase):

    def test_getAuthresponse(self):
        response = getAuthresponse(AUTH_URL, CLIENT_ID, CLIENT_SECRET)
        self.assertEqual(response.status_code, 200)
        response1 = getAuthresponse('https://accounts.spotify.com/api/',
                                    CLIENT_ID, CLIENT_SECRET)
        self.assertNotEqual(response1.status_code, 200)
        response2 = getAuthresponse(AUTH_URL,
                                    '7bb5a610971f437690b91981206',
                                    CLIENT_SECRET)
        self.assertNotEqual(response2.status_code, 200)
        response3 = getAuthresponse(AUTH_URL, CLIENT_ID,
                                    'f102316e6e7b45bd93e1988be3162')
        self.assertNotEqual(response3.status_code, 200)


    def test_convertToJson(self):
        json = convertToJson(BASE_URL, artist_id, AUTH_URL, CLIENT_ID,
                             CLIENT_SECRET)
        # other artist
        json2 = convertToJson(BASE_URL, '0cGUm45nv7Z6M6qdXYQGTX', AUTH_URL,
                               CLIENT_ID, CLIENT_SECRET)
        self.assertNotEqual(json, None)
        self.assertNotEqual(json, json2)
        self.assertEqual(type(json), dict)


    def test_convertToJsonT(self):
        json = convertToJsonT(BASE_URL, artist_id, AUTH_URL, CLIENT_ID,
                              CLIENT_SECRET)
        # other artist
        json2 = convertToJsonT(BASE_URL, '0cGUm45nv7Z6M6qdXYQGTX', AUTH_URL,
                               CLIENT_ID, CLIENT_SECRET)
        self.assertNotEqual(json, None)
        self.assertNotEqual(json, json2)
        self.assertEqual(type(json), dict)


if __name__ == '__main__':
    unittest.main()
