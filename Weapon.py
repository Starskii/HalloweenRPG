from abc import abstractmethod
from random import uniform


# This is the abstract parent class for all weapons
class Weapon:
    _durability = None
    _attackmultiplier = None
    _player = None
    _name = None

    @abstractmethod
    def __init__(self):
        pass

    def use(self):
        if isinstance(self, HersheyKiss):
            self._durability -= 0
        else:
            self._durability -= 1
        if self._durability <= 0:
            self._player.weaponbroke(self)

    def getname(self):
        return self._name

    def getdurability(self):
        return self._durability

    def getattackmultiplier(self):
        return self._attackmultiplier


class HersheyKiss(Weapon):
    def __init__(self, player):
        self._durability = 1
        self._attackmultiplier = 1.0
        self._player = player
        self._name = "HersheyKiss"


class SourStraw(Weapon):
    def __init__(self, player):
        self._attackmultiplier = uniform(1.0, 1.75)
        self._durability = 2
        self._player = player
        self._name = "SourStraw"


class ChocolateBar(Weapon):
    def __init__(self, player):
        self._attackmultiplier = uniform(2.0, 2.4)
        self._durability = 4
        self._player = player
        self._name = "ChocolateBar"


class NerdBomb(Weapon):
    def __init__(self, player):
        self._attackmultiplier = uniform(3.5, 5.0)
        self._durability = 1
        self._player = player
        self._name = "NerdBomb"
