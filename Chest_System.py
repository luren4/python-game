import random
class Chest_class:
    def open_chest(self, w, a, r, l):
        #Self skippar första, w => weapon, a=> armor, r=> ring, l=> level

        new_weapon = (w + random.randint(1, 30)) + 2 * l
        new_armour = (a + random.randint(1, 30)) + 2 * l
        new_ring = round((r + 0.1 * random.randint(1, 3) + 0.1 * l), 2)

 
        print("             Du hittade en kista!             ")
        print("________________________________________________")
        print(f"Du får välja en av sakerna i den magiska kistan")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("\n\n\n\n")
        




        print("             Välj en av nedanstående                                   Ditt inventory just nu             ")
        print("________________________________________________            ________________________________________________")
        print(f"Val 1  *  nytt vapen med {new_weapon} damage                         Ditt svärd har nu {w} damage")
        print(f"Val 2  *  ny armor med {new_armour} i skydd                          Din rustning har nu {a} i skydd")
        print(f"Val 3  *  ny ring med {new_ring} gånger din damage                 Din ring har nu {r} gånger din damage")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("\n\n")

        NewAcessoryChoice = int(input("Välj ditt val --->  "))

        if NewAcessoryChoice == 1:
            return (new_weapon, a, r)

        if NewAcessoryChoice == 2:
            return (w, new_armour, r)

        if NewAcessoryChoice == 3:
            return (w, a, new_ring)
