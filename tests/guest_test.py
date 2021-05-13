import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Mario", "Castle Theme", 100.00)

    def test_guest_has_name(self):
        self.assertEqual("Mario", self.guest.name)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Castle Theme", self.guest.favourite_song)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest.wallet)