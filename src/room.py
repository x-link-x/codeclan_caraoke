class Room:
    
    def __init__(self, name):
        self.name = name
        self.guests = {}


    def check_in_guest(self, guest):
        self.guests[guest.name] = guest.favourite_song

    def check_out_guest(self, guest):
        self.guests.pop(guest.name)
