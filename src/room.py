class Room:
    
    def __init__(self, name):
        self.name = name
        self.guests = {}
        self.playlist = []
        self.entry_fee = 10.00
        self.tab = 0.00

    def check_in_guest(self, guest):
        if len(self.guests) < 4:
            self.guests[guest] = guest.favourite_song
            guest.pay_entry_fee(self)
        else:
            return "Sorry, the room is full"

    def check_out_guest(self, guest):
        self.guests.pop(guest)

    def add_song_to_room(self, song):
        self.playlist.append(song)

    def guest_cheers(self, guest):
        for song in self.guests.values():
            if song in self.playlist:
                return guest.cheer()
        
    def guest_sings_a_song(self, song, guest):
        self.playlist.remove(song)
        guest.sing(song)
        