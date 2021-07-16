import unittest
from bad_flow import getAuthresponse, convertToJson, convertToJsonT


AUTH_URL = 'https://accounts.spotify.com/api/token'
CLIENT_ID = '7bb5a610971f437690b91981206e0025'
CLIENT_SECRET = 'f102316e6e7b45bd93e1988be3162cf6'


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


if __name__ == '__main__':
    unittest.main()
