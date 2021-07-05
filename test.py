import unittest
from bad_flow import getAuthresponse, getAccessToken, convertToJson, displayTitle, displayAlbum, getHeader, convertToJsonTrack, displayTopTracks, convertToDataFrame  


class TestFileName(unittest.TestCase):
    def test_getAuthresponse(self):
      getAuthresponse('https://accounts.spotify.com/api/token',
                      '7bb5a610971f437690b91981206e0025',
                      'f102316e6e7b45bd93e1988be3162cf6')


    def test_displayTitle(self):
        self.assertTrue(displayTitle('hi'))


if __name__ == '__main__':
    unittest.main()
