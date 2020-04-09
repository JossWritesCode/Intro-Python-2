

# imports

from room import Room
from item import Item
from player import Player
import textwrap
import colorama
from colorama import Fore, Style


# welcome message

print("Welcome to my dungeon \n")

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'gold':  Item("Gold",
                  "A piece of gold flickers under the light."),

    'sword':    Item("Sword", """It's dangerous to go alone! Take this!"""),

    'goblet': Item("Goblet", """A jeweled cup lies as if in wait for its king or queen."""),

    'necklace':   Item("Necklace", """Sparkling gems adorn this delicate necklace."""),

    'scepter': Item("Scepter", """The knowledge of what great monarch held this majestic scepter has been lost to time."""),
}


# Link rooms together

def link_room(current_room, direction, next_room):
    setattr(room[current_room], direction, room[next_room])


link_room('outside', 'n_to', 'foyer')
link_room('foyer', 's_to', 'outside')
link_room('foyer', 'n_to', 'overlook')
link_room('foyer', 'e_to', 'narrow')
link_room('overlook', 's_to', 'foyer')
link_room('narrow', 'w_to', 'foyer')
link_room('narrow', 'n_to', 'treasure')
link_room('treasure', 's_to', 'narrow')


# Add items to rooms

room["foyer"].add_item(item["sword"])
room["overlook"].add_item(item["gold"])
room["overlook"].add_item(item["scepter"])
room["narrow"].add_item(item["necklace"])
room["narrow"].add_item(item["goblet"])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

me = Player("Joscelyn", room["outside"])


def describe():
    print(Style.RESET_ALL + "You are in the " + me.current_room.name + "\n")
    print(textwrap.dedent(me.current_room.description).strip() + "\n")
    if len(me.current_room.list_of_items) > 0:
        for item in me.current_room.list_of_items:
            print(
                f"You find a {item.name}. \n {textwrap.dedent(item.description).strip()} \n")


def explore():
    user = 5
    while not user == "q":
        describe()
        user = input(
            "[n] North   [e] East    [s] South    [w] West       [q] Quit\n")
        print("Please choose to continue... \n")

        # user chooses North
        if user == "n":
            if me.current_room.n_to != None:
                me.current_room = me.current_room.n_to
            else:
                print(Fore.RED + "Sorry there is no room to the north \n")

        # user chooses East
        elif user == "e":
            if me.current_room.e_to != None:
                me.current_room = me.current_room.e_to
            else:
                print(Fore.RED + "Sorry there is no room to the east \n")

        # user chooses South
        elif user == "s":
            if me.current_room.s_to != None:
                me.current_room = me.current_room.s_to
            else:
                print(Fore.RED + "Sorry there is no room to the south \n")

        # user chooses West
        elif user == "w":
            if me.current_room.w_to != None:
                me.current_room = me.current_room.w_to
            else:
                print(Fore.RED + "Sorry there is no room to the west \n")

        elif user == 5:
            pass

        else:
            print(Fore.RED + "Invalid selection. Please try again. \n")


explore()
