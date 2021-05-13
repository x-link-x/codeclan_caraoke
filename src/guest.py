class Guest:
    
    def __init__(self, name, favourite_song, wallet):
        self.name = name
        self.favourite_song = favourite_song
        self.wallet = wallet

    def can_afford_entry_fee(self, room):
        return self.wallet >= room.entry_fee

    def pay_entry_fee(self, room):
        if self.can_afford_entry_fee(room):
            self.wallet -= room.entry_fee
            room.tab += room.entry_fee

    def cheer(self):
        return "Woop!"

    def sing(self, song):
        return "Singing..."
        