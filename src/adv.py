

# file i/o functions for historical results

from room import Room
from player import Player
import textwrap


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

print("Welcome to my dungeon, {player.name}!")
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

# user = int(
#     input("[1] North   [2] East    [3] South    [4] West       [9] Quit\n"))


# Make a new player object that is currently in the 'outside' room.

me = Player("Joscelyn", "outside")

# Write a loop that:
#

me.current_room_info = room[me.current_room]


def describe():
    print(me.name)
    print(me.current_room)
    print(textwrap.dedent(me.current_room_info.description).strip())


describe()


def explore():
    while not user == 9:
        # user chooses North
        if user == 1:
            me.current_room = room[me.current_room].n_to
            describe()
        # user chooses East
        elif user == 2:
            me.current_room = room[me.current_room].e_to
            describe()
        # user chooses South
        elif user == 3:
            me.current_room = room[me.current_room].s_to
            describe()
        # user chooses South
        elif user == 3:
            me.current_room = room[me.current_room].s_to
            describe()
        else:
            print("Invalid selection. Please try again.")


# explore()


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
