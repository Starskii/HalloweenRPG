from random import *
from Weapon import *

# This class is a data structure that handles values related to the player
class Player:
    _health = None
    _attack = None
    _playerCol = None
    _playerRow = None
    _inventory = []
    _game = None

    def __init__(self, game):
        self._game = game
        self._playerCol = 0
        self._playerRow = 0
        self._health = uniform(100.0, 125.0)
        self._attack = uniform(10.0, 20.0)
        for x in range(10):
            weapontype = randint(0, 2)
            if weapontype is 0:
                self._inventory.append(SourStraw(self))
            elif weapontype is 1:
                self._inventory.append(ChocolateBar(self))
            else:
                self._inventory.append(NerdBomb(self))
        self._inventory[0] = HersheyKiss(self)

    # This method is called when a weapon has been broken
    def weaponbroke(self, weapon):
        self._inventory.remove(weapon)

    # Returns the location of the player as a tuple
    def getlocation(self):
        return self._playerCol, self._playerRow

    # Moves the player up
    def moveup(self):
        self._playerRow -= 1

    # Moves the player down
    def movedown(self):
        self._playerRow += 1

    # Moves the player right
    def moveright(self):
        self._playerCol += 1

    # Moves the player left
    def moveleft(self):
        self._playerCol -= 1

    # Returns the inventory of the player
    def getinventory(self):
        return self._inventory

    # Returns the players damage
    def getdamage(self):
        return self._attack

    # This method is called when the player takes damage
    def receivedamage(self, damage):
        self._health -= damage
        if self._health <= 0:
            self._game.gamelost()

    # Returns the health of the player
    def gethealth(self):
        return self._health
