import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Mario", "Castle Theme")


    def test_guest_has_name(self):
        self.assertEqual("Mario", self.guest.name)