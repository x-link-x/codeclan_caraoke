import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Nintendo")
        self.guest_1 = Guest("Mario", "Castle Theme", 100.00)
        self.guest_2 = Guest("Luigi", "Dolphin Shoals", 30.00)
        self.guest_3 = Guest("Toad", "Gusty Garden Galaxy", 5.00)
        self.guest_4 = Guest("Peach", "Rosalina in the Observatory", 70.00)
        self.guest_5 = Guest("Bowser", "A Boss Approaches", 40.00)

    def test_room_name_is_room_1(self):
        self.assertEqual("Nintendo", self.room.name)

    def test_room_has_dictionary_of_guests(self):
        self.assertEqual({}, self.room.guests)

    def test_room_can_check_in_guests(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual({"Mario": "Castle Theme"}, self.room.guests)

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
        self.assertEqual({"Luigi": "Dolphin Shoals"}, self.room.guests)

    def test_room_can_add_songs(self):
        self.room.add_song_to_room("Dolphin Shoals")
        self.assertEqual(["Dolphin Shoals"], self.room.songs)

    def test_room_tab_increases_when_guest_is_checked_in(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(10.00, self.room.tab)

    def test_guest_cannot_enter_if_no_entry_fee(self):
        self.room.check_in_guest(self.guest_3)
        self.assertEqual(0.00, self.room.tab)



    

    