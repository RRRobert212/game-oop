#inventory.py

from constants import *

class Inventory:
    
    def __init__(self):

        self.weapons = []
        self.armor = []
        self.consumables = []

    def add_weapon(self, weapon_id):
        """takes weapon_id as input, appends [weapon id, weapon name] to weapons inventory"""
        self.weapons.append([weapon_id, weapon_types[weapon_id]])

    def display_inventory(self):

        print()
        print("INVENTORY:")

        self.display_weapons()
        self.display_armor()
        self.display_consumables()


    def display_weapons(self):
        print("Weapons: ", end = '')
        if len(self.weapons) == 0: print("None.")
        else:
            for index, weapon in enumerate(self.weapons, start=1):
                print(f"{index}. {weapon[1]}", end = '  ')  # Display the weapon with its corresponding number

            print()
    def display_armor(self):
        print("Armor: ", end ='')
        if len(self.armor) == 0: print("None")
        else:
            for index, armor in enumerate(self.armor, start =1):
                print(f"{index}. {armor[1]}", end = "   ")
            print()
    def display_consumables(self):
        print("Consumables: ", end = '')
        if len(self.consumables) == 0: print("None")
        else:
            for index, consumable in enumerate(self.consumables, start =1):
                print(f"{index}. {consumable[1]}", end = "   ")
                
            print()



    def add_armor(self, armor_id):
        """takes armor_id as input, append [armor id, armor name] to armor inventory"""
        self.armor.append([armor_id, armor_types[armor_id]])

    def add_consumbale(self, consumbale_id):
        """takes armor_id as input, append [armor id, armor name] to armor inventory"""
        self.consumable.append([consumbale_id, consumable_types[consumbale_id]])




