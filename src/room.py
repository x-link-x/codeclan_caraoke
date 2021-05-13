class Room:
    
    def __init__(self, name):
        self.name = name
        self.guests = {}
        self.songs = []
        self.entry_fee = 10.00
        self.tab = 0.00

    def check_in_guest(self, guest):
        if len(self.guests) < 4:
            self.guests[guest.name] = guest.favourite_song
            guest.pay_entry_fee(self)
        else:
            return "Sorry, the room is full"

    def check_out_guest(self, guest):
        self.guests.pop(guest.name)

    def add_song_to_room(self, song):
        self.songs.append(song)
