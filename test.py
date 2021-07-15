import unittest
from bad_flow import getAuthresponse

class TestFileName(unittest.TestCase):
    def test_getAuthresponse(self):
      response = getAuthresponse('https://accounts.spotify.com/api/token',
                      '7bb5a610971f437690b91981206e0025',
                      'f102316e6e7b45bd93e1988be3162cf6')
      self.assertEqual(response, 
                       requests.post(https://accounts.spotify.com/api/token, {
                         'grant_type': 'client_credentials',
                         'client_id': '7bb5a610971f437690b91981206e0025',
                         'client_secret': 'f102316e6e7b45bd93e1988be3162cf6',
                       }))


if __name__ == '__main__':
    unittest.main()
