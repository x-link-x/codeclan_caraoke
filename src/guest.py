class Guest:
    
    def __init__(self, name, favourite_song, wallet):
        self.name = name
        self.favourite_song = favourite_song
        self.wallet = wallet


    def pay_entry_fee(self, room):
        self.wallet -= room.entry_fee
        