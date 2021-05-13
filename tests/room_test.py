import unittest
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Room 1")


    def test_room_name_is_room_1(self):
        self.assertEqual("Room 1", self.room_1.name)