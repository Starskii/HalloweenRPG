from Game import *
game = Game()

# This module functions as the driver for the game.
while game.gamestatus() is False:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    game.displaymap()
    print("\n What would you like to do? ")
    print(" You can move up 'u', down 'd', left 'l', and right 'r'")
    ui = input("\n\tEnter your choice: ")
    game.moveplayer(ui)
    if game.checkplayerathouse():
        game.startbattle()
    game.checkwin()
if game._gamewon is True:
    print("You won!")
else:
    print("You lost!")