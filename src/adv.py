

# imports

from room import Room
from item import Item
from player import Player
import textwrap
import colorama
from colorama import Fore, Style


# welcome message

print(Fore.MAGENTA + "\n \n Welcome to my dungeon \n \n")

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

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
    'gold':  Item("Gold Piece",
                  "A piece of gold flickers under the light."),

    'sword':    Item("Sword", """It's dangerous to go alone! Take this!"""),

    'goblet': Item("Goblet", """A jeweled cup lies as if in wait for its king or queen."""),

    'necklace':   Item("Necklace", """Sparkling gems adorn this delicate necklace."""),

    'scepter': Item("Scepter", """All knowledge of the great monarch who held this majestic scepter has been lost to time."""),
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
    print(Style.RESET_ALL + "You are in the " +
          Fore.CYAN + me.current_room.name + "\n" + "\n" + Style.RESET_ALL)
    print(textwrap.dedent(me.current_room.description).strip() + "\n" + "\n")


def offer_item_to_player(item):
    want_item = input("Do you want to take this item? [y] Yes   [n] No \n \n")
    if want_item == 'y':
        me.add_item(item)
        print(
            f"You put the {item.name} in your bag. Who knows when you'll need it. \n \n")
    elif want_item == 'n':
        print(
            f"You leave the {item.name} for future adventurers. They might need it more than you. \n \n")


def describe_item_to_player(item):
    print("You find a " + Fore.GREEN +
          item.name + Style.RESET_ALL + "." + "\n")
    print(textwrap.dedent(item.description).strip() + "\n" + "\n")


def explore():
    user = 5
    while not user == 9:
        describe()
        if len(me.current_room.list_of_items) > 0:
            for item in me.current_room.list_of_items:
                describe_item_to_player(item)
                offer_item_to_player(item)

        user = int(input(
            "[1] North   [2] East   [3] South   [4] West      [9] quit   \n \n"))

        # user chooses North
        if user == 1:
            if me.current_room.n_to != None:
                me.current_room = me.current_room.n_to

            else:
                print(Fore.RED + "Sorry there is no room to the north \n \n")

        # user chooses East
        elif user == 2:
            if me.current_room.e_to != None:
                me.current_room = me.current_room.e_to
            else:
                print(Fore.RED + "Sorry there is no room to the east \n \n")

        # user chooses South
        elif user == 3:
            if me.current_room.s_to != None:
                me.current_room = me.current_room.s_to
            else:
                print(Fore.RED + "Sorry there is no room to the south \n \n")

        # user chooses West
        elif user == 4:
            if me.current_room.w_to != None:
                me.current_room = me.current_room.w_to
            else:
                print(Fore.RED + "Sorry there is no room to the west \n \n")

        elif user == 5:
            pass

        elif user == 9:
            pass

        else:
            print(Fore.RED + "Invalid selection. Please try again. \n \n")


explore()
