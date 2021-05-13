import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Castle Theme")

    def test_song_has_title(self):
        self.assertEqual("Castle Theme", self.song.title)
        