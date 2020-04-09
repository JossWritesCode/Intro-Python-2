

# file i/o functions for historical results

from room import Room
from player import Player
import textwrap
import colorama
from colorama import Fore, Style


def load_results():
    text_file = open("history.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history


def save_results(w, t, l):
    text_file = open("history.txt", "w")
    text_file.write(str(w) + "," + str(t) + "," + str(l))
    text_file.close()


# welcome message

print("Welcome to my dungeon \n")
print("Please choose to continue...")


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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

me = Player("Joscelyn", room["outside"])


def describe():
    print(Style.RESET_ALL + textwrap.dedent(me.current_room.description).strip() + "\n")


def explore():
    user = 5
    while not user == 9:
        describe()
        user = int(
            input("[1] North   [2] East    [3] South    [4] West       [9] Quit\n"))
        # user chooses North
        if user == 1:
            if me.current_room.n_to != None:
                me.current_room = me.current_room.n_to
            else:
                print(Fore.RED + "Sorry there is no room to the north \n")

        # user chooses East
        elif user == 2:
            if me.current_room.e_to != None:
                me.current_room = me.current_room.e_to
            else:
                print(Fore.RED + "Sorry there is no room to the east \n")

        # user chooses South
        elif user == 3:
            if me.current_room.s_to != None:
                me.current_room = me.current_room.s_to
            else:
                print(Fore.RED + "Sorry there is no room to the south \n")

        # user chooses West
        elif user == 4:
            if me.current_room.w_to != None:
                me.current_room = me.current_room.w_to
            else:
                print(Fore.RED + "Sorry there is no room to the west \n")

        elif user == 5:
            pass

        else:
            print("\033[1;31;40m Invalid selection. Please try again. \n")


explore()


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
