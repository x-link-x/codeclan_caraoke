import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Nintendo")

        self.song_1 = Song("Castle Theme")
        self.song_2 = Song("Dolphin Shoals")
        self.song_3 = Song("Gusty Garden Galaxy")
        self.song_4 = Song("Rosalina in the Observatory")
        self.song_5 = Song("A Boss Approaches")

        self.guest_1 = Guest("Mario", self.song_1, 100.00)
        self.guest_2 = Guest("Luigi", self.song_2, 30.00)
        self.guest_3 = Guest("Toad", self.song_3, 5.00)
        self.guest_4 = Guest("Peach", self.song_4, 70.00)
        self.guest_5 = Guest("Bowser", self.song_5, 40.00)

    def test_room_name_is_room_1(self):
        self.assertEqual("Nintendo", self.room.name)

    def test_room_has_dictionary_of_guests(self):
        self.assertEqual({}, self.room.guests)

    def test_room_can_check_in_guests(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual({self.guest_1: self.song_1}, self.room.guests)

    def test_checkin_does_not_exceed_maximum_capacity(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.room.check_in_guest(self.guest_3)
        self.room.check_in_guest(self.guest_4)
        self.room.check_in_guest(self.guest_5)
        self.assertEqual(4, len(self.room.guests))

    def test_room_returns_message_when_full(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.room.check_in_guest(self.guest_3)
        self.room.check_in_guest(self.guest_4)
        self.assertEqual("Sorry, the room is full", self.room.check_in_guest(self.guest_5))

    def test_room_can_check_out_guests(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.room.check_out_guest(self.guest_1)
        self.assertEqual({self.guest_2: self.song_2}, self.room.guests)

    def test_room_can_add_songs(self):
        self.room.add_song_to_room(self.song_2)
        self.assertEqual([self.song_2], self.room.playlist)

    def test_room_tab_increases_when_guest_is_checked_in(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(10.00, self.room.tab)

    def test_guest_cannot_enter_if_no_entry_fee(self):
        self.room.check_in_guest(self.guest_3)
        self.assertEqual(0.00, self.room.tab)

    def test_guest_cheers_if_favourite_song_in_playlist(self):
        self.room.add_song_to_room(self.song_4)
        self.room.check_in_guest(self.guest_4)
        self.assertEqual("Woop!", self.room.guest_cheers(self.guest_4))

    def test_guest_can_sing_song(self):
        self.room.add_song_to_room(self.song_2)
        self.room.check_in_guest(self.guest_2)
        self.room.guest_sings_a_song(self.song_2, self.guest_2)
        self.assertEqual("Singing...", self.guest_2.sing(self.song_2))
        self.assertEqual([], self.room.playlist)

    