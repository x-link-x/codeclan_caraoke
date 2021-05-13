import unittest
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room 1")


    def test_room_name_is_room_1(self):
        self.assertEqual("Room 1", self.room.name)

    def test_room_has_dictionary_of_guests(self):
        self.assertEqual({}, self.room.guests)