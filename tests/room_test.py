import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room 1")
        self.guest_1 = Guest("Mario", "Castle Theme")

    def test_room_name_is_room_1(self):
        self.assertEqual("Room 1", self.room.name)

    def test_room_has_dictionary_of_guests(self):
        self.assertEqual({}, self.room.guests)

    def test_room_can_check_in_guests(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual({"Mario": "Castle Theme"}, self.room.guests)

    