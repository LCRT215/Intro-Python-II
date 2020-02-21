from room import Room  # getting the room object from Room
from player import Player  # getting the player object form Player
import sys  # to be able to exit the game

# Declare all the rooms

room = {
    'outside':  Room("🗿 Outside Cave Entrance 🗿",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("🏜 Foyer 🏜", """Dim light filters in from the south. Dusty
                    passages run north and east."""),

    'overlook': Room("🏔 Grand Overlook 🏔", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm."""),

    'narrow':   Room("🗻 Narrow Passage 🗻", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air."""),

    'treasure': Room("🏆 Treasure Chamber 🏆", """You've found the long-lost treasure
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

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def newPlayer():
    return Player(current_room=room['outside'])


player = newPlayer()
# ^ store player class in player vairable to be used below


def movePlayer(player):
    print(f'{player.current_room}')

    playersMove = player.move()
    # ^ passed players move through player class

    stop = "=========== 🚫 Oh No!!! You can't go that way! Make another move 🚫 ============"

    moveDirection = ""

    # wannaMove = input(
    #         '\n\nWhich way would you like to go?\n\nn - North\ns - South\ne - East\nw - West\n\n \n\nType Here==>   ')

    # ^ save players selected move direction here
    while moveDirection not in playersMove.keys():
        moveDirection = input(
            '\n\nWhich way would you like to go?\n\nn - North\ns - South\ne - East\nw - West\n\n \n\nType Here==>   ')
        if moveDirection == 'stop':
            print('======= 👋 You have exited the game. See ya later! 👋 =======')
            sys.exit()

# move commands
        try:
            if moveDirection == 'n':
                player.current_room = player.current_room.n_to
            if moveDirection == 's':
                player.current_room = player.current_room.s_to
            if moveDirection == 'e':
                player.current_room = player.current_room.e_to
            if moveDirection == 'w':
                player.current_room = player.current_room.w_to
        except AttributeError:
            # ^ AttributeError can be defined as an error that is raised when an attribute reference or assignment fails
            print(stop)
        # print(f'{player.current_room}')
        # return (movePlayer(player))


play = ""
while play is not 'stop':
    movePlayer(player)
