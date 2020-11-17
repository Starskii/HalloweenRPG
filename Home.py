from random import randint

from NPC import *


class Home:
    _monsters = []
    _monsterpopulation = 0
    _neighborhood = None

    # Constructor
    def __init__(self, neighborhood):
        self._monsters = []
        numberofmonsters = randint(0, 10)
        for x in range(numberofmonsters):
            monstertype = randint(0, 4)
            if monstertype is 0:
                npc = Person(self)
            elif monstertype is 1:
                npc = Zombie(self)
                self._monsterpopulation += 1
            elif monstertype is 2:
                npc = Vampire(self)
                self._monsterpopulation += 1
            elif monstertype is 3:
                npc = Ghoul(self)
                self._monsterpopulation += 1
            else:
                npc = Werewolf(self)
                self._monsterpopulation += 1
            self._monsters.append(npc)
        self._neighborhood = neighborhood
        self._neighborhood.addmonsterpopulation(self._monsterpopulation)

    # Returns the monsters in a given home
    def getmonsters(self):
        return self._monsters

    # Returns the number of monsters in a given home
    def getmonsterpopulation(self):
        return self._monsterpopulation

    # This is the function the observed NPC class calls to alert the Home object that a monster has died.
    def monsterdied(self, monster):
        self._monsters.remove(monster)
        self._monsters.append(Person(self))
        self._monsterpopulation -= 1
        self._neighborhood.updatemonsterpopulation()

