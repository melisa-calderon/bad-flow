import unittest
from bad_flow import convertToJson, displayTitle, displayAlbum


class TestFileName(unittest.TestCase):
    def test_convertToJson(self):
        self.assertTrue(convertToJson('https://api.spotify.com/v1/', '5cj0lLjcoR7YOSnhnX0Po5') )

    def test_displayTitle(self):
        self.assertTrue(displayTitle('hi'))
        #self.assertEqual(displayTitle(''), )

if __name__ == '__main__':
    unittest.main()