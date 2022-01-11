import random
from Chest_System import Chest_class
from GrafikerOchText import grafik

#Startvärden för spelaren
chest =  Chest_class()
class Player_class:
    def __init__(self) -> None:
        self.weapon = 100
        self.armour = 100
        self.ring = 1
        self.level = 1

player = Player_class()





grafik = grafiker()

grafik.welcometext()


# print("\n"*40)

# print("             Welcome to DungeonKeep             ")
# print("________________________________________________")
# print("\n"*15)
# int(input("lol-->"))

print("\n"*40)







#Tillfällig loop
keepgoing = 0
while keepgoing == 0:
    #Här hittar spelaren en kista.
    player.weapon, player.armour, player.ring = chest.open_chest(player.weapon, player.armour, player.ring, player.level)
    player.level += 1
    print("\n"*40)
    # print("-------------Ditt inventory just nu----------")
    # print("---------------------------------------------")
    # print(f"Ditt svärd har nu {player.ring} damage")
    # print(f"Din rustning har nu {player.armour} i skydd")
    # print(f"Din ring har nu {player.ring} gånger din damage")
    # print("---------------------------------------------")
    # print("---------------------------------------------")
    # print("\n"*9)
    #print(player.level)






