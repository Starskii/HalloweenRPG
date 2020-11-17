from Home import *
from Player import *


class Neighborhood:
    _grid = [[None for i in range(4)] for j in range(4)]
    _monsterpopulation = 0
    _game = None
    _player = None

    # Constructor
    def __init__(self, cols, rows, game, player):
        self._grid = [[0 for i in range(cols)] for j in range(rows)]
        for x in range(cols):
            for y in range(rows):
                obj = None
                placement = randint(0, 3)
                if placement is 0:
                    obj = Home(self)
                else:
                    obj = 0
                self._grid[x][y] = obj
        self._grid[0][0] = 0
        self._game = game
        self._player = player

    # Updates the population field of this object when monsters have been added to the Home
    def addmonsterpopulation(self, pop):
        self._monsterpopulation += pop

    # This updates monster population to reflect potential deaths
    def updatemonsterpopulation(self):
        self._monsterpopulation -= 1
        if self._monsterpopulation <= 0:
            self._game.gamewon()

    # Returns the monster population of the neighborhood
    def getmonsterpopulation(self):
        return self._monsterpopulation

    # Returns the game grid/map
    def getgrid(self):
        return self._grid
