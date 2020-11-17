from Neighborhood import *

from Player import *


# Game Class handles most Game logic
class Game:
    _sizeCol = 4
    _sizeRow = 4
    _neighborhood = None
    _player = None
    _gameover = False
    _gamewon = False

    def __init__(self):
        self._player = Player(self)
        self._neighborhood = Neighborhood(self._sizeCol, self._sizeRow, self, self._player)

    # Checks if the player has won
    def checkwin(self):
        pop = self._neighborhood.getmonsterpopulation()
        if pop <= 0:
            self.gamewon()

    # Declares that the game has been won
    def gamewon(self):
        self._gameover = True
        self._gamewon = True

    # Declares that the game has been lost
    def gamelost(self):
        self._gameover = True

    # Returns the status of the game
    def gamestatus(self):
        return self._gameover

    # Displays the map, H = Home, C = Completed Home, _ is empty and P is for the player
    def displaymap(self):
        grid = self._neighborhood.getgrid()
        playerlocation = self._player.getlocation()
        for row in range(self._sizeCol):
            line = ""
            for col in range(self._sizeRow):
                currentlocation = (col, row)
                if playerlocation == currentlocation:
                    line += "P "
                elif isinstance(grid[col][row], Home):
                    if grid[col][row].getmonsterpopulation() > 0:
                        line += "H "
                    else:
                        line += "C "
                else:
                    line += "_ "
            print(line)

    # This function checks the condition of whether the player is currently at a house
    def checkplayerathouse(self):
        playerlocation = self._player.getlocation()
        if isinstance(self._neighborhood.getgrid()[playerlocation[0]][playerlocation[1]], Home):
            if self._neighborhood.getgrid()[playerlocation[0]][playerlocation[1]].getmonsterpopulation() > 0:
                return True
            else:
                return False
        else:
            return False

    # This is the battle function for the game
    def startbattle(self):
        inbattle = True
        while inbattle:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
            hp = self._player.gethealth()
            print("Your health is: " + str(hp))
            home = self._neighborhood.getgrid()[self._player.getlocation()[0]][self._player.getlocation()[1]]
            personcount = 0
            zombiecount = 0
            vampirecount = 0
            ghoulcount = 0
            werewolfcount = 0
            for monster in home.getmonsters():
                if isinstance(monster, Person):
                    personcount += 1
                elif isinstance(monster, Zombie):
                    zombiecount += 1
                elif isinstance(monster, Vampire):
                    vampirecount += 1
                elif isinstance(monster, Ghoul):
                    ghoulcount += 1
                else:
                    werewolfcount += 1

            print("There is " + str(personcount) +
                " people, " + str(zombiecount) +
                " zombies " + str(vampirecount) +
                " vampires " + str(werewolfcount) +
                " werewolfs and " + str(ghoulcount) +
                " ghouls.")

            print("Pick your weapon (0-10): ")

            count = 0
            for weapon in self._player.getinventory():
                print(str(count) + ": " + weapon.getname() + " durability: " + str(weapon.getdurability()))
                count += 1

            validchoice = False
            userChoice = 0
            while validchoice == False:
                ui = input("Select Attack: ")
                try:
                    userChoice = int(ui)
                    if len(self._player.getinventory()) > userChoice >= 0:
                        validchoice = True
                    else:
                        print("Not valid input")
                except:
                    print("Not valid input")

            weapon = self._player.getinventory()[int(userChoice)]
            weapon.use()
            for monster in home.getmonsters():
                monster.receiveattack(self._player.getdamage(), weapon)
                self._player.receivedamage(monster.attack())

            if home.getmonsterpopulation() <= 0:
                inbattle = False
            elif self._player.gethealth() <= 0:
                inbattle = False

    # Moves and handles errors regarding player movement on the map
    def moveplayer(self, ui):
        if ui is "u":
            if self._player.getlocation()[1] > 0:
                self._player.moveup()
        elif ui is "d":
            if self._player.getlocation()[1] < (self._sizeCol-1):
                self._player.movedown()
        elif ui is "l":
            if self._player.getlocation()[0] > 0:
                self._player.moveleft()
        elif ui is "r":
            if self._player.getlocation()[0] < (self._sizeRow-1):
                self._player.moveright()