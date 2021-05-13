import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song = Song("Castle Theme")
        self.guest = Guest("Mario", self.song.title, 100.00)
        self.room = Room("Nintendo")

    def test_guest_has_name(self):
        self.assertEqual("Mario", self.guest.name)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Castle Theme", self.guest.favourite_song)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest.wallet)

    def test_pay_entry_fee_removes_money_from_wallet(self):
        self.guest.pay_entry_fee(self.room)
        self.assertEqual(90.00, self.guest.wallet)

    def test_guest_can_cheer(self):
        self.assertEqual("Woop!", self.guest.cheer())