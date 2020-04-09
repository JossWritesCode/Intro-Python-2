# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, current_room):
        self.name = "Player 1"
        self.current_room = current_room
        self.current_room_info = None
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def set_name(self, name):
        self.name = name
