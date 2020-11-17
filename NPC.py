from abc import abstractmethod
from random import *
from Weapon import *


# Abstract class that serves as the parent class for all NPC
class NPC:
    _health = None
    _attack = None
    _home = None

    # Constructor
    @abstractmethod
    def __init__(self):
        pass

    # Required attack method
    @abstractmethod
    def attack(self):
        pass

    # This is where the NPC notifies it's observer (the house)
    # that it has died.
    def receiveattack(self, damage, weapon):
        if isinstance(self, Person):
            damage = 0
        elif isinstance(self, Zombie) and isinstance(weapon, SourStraw):
            damage = damage*2
        elif isinstance(self, Vampire) and isinstance(weapon, ChocolateBar):
            damage = 0
        elif isinstance(self, Ghoul) and isinstance(weapon, NerdBomb):
            damage = damage*5
        elif isinstance(self, Werewolf) and (isinstance(weapon, ChocolateBar) or isinstance(weapon, SourStraw)):
            damage = 0
        self._health -= damage*weapon.getattackmultiplier()
        if self._health <= 0:
            self._home.monsterdied(self)

# This is the Person class
class Person(NPC):
    def __init__(self, home):
        self._health = 100.0
        self._attack = -10
        self._home = home

    def attack(self):
        return self._attack

# This is the Zombie class
class Zombie(NPC):
    def __init__(self, home):
        self._health = uniform(50.0, 100.0)
        self._attack = 10
        self._home = home

    def attack(self):
        return uniform(0.0, self._attack)

# This is the Vampire class
class Vampire(NPC):
    def __init__(self, home):
        self._health = uniform(100.0, 200.0)
        self._attack = 20
        self._home = home

    def attack(self):
        return uniform(10.0, self._attack)

# This is the Ghoul class
class Ghoul(NPC):
    def __init__(self, home):
        self._health = uniform(40.0, 80.0)
        self._attack = 20
        self._home = home

    def attack(self):
        return uniform(15.0, 30.0)

# This is the Werewolf class
class Werewolf(NPC):
    def __init__(self, home):
        self._health = 200.0
        self._attack = 40.0
        self._home = home

    def attack(self):
        return uniform(0.0, self._attack)
