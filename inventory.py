#inventory.py

from constants import *

class Inventory:
    
    def __init__(self):

        self.weapons = []
        self.armor = []
        self.consumables = []

    def add_weapon(self, weapon_id):
        """takes weapon_id as input, appends [weapon id] to weapons inventory"""
        self.weapons.append(weapon_id)

    def add_armor(self, armor_id):
        """takes armor_id as input, append [armor id, armor name] to armor inventory"""
        self.armor.append(armor_id)

    def add_consumbale(self, consumbale_id):
        """takes armor_id as input, append [armor id, armor name] to armor inventory"""
        self.consumables.append(consumbale_id)



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
            for index, weapon_id in enumerate(self.weapons, start=1):
                print(f"{index}. {weapon_names[weapon_id]}", end = '  ')  # Display the weapon with its corresponding number

            print()
    def display_armor(self):
        print("Armor: ", end ='')
        if len(self.armor) == 0: print("None")
        else:
            for index, armor_id in enumerate(self.armor, start =1):
                print(f"{index}. {armor_names[armor_id]}", end = "   ")
            print()
    def display_consumables(self):
        print("Consumables: ", end = '')
        if len(self.consumables) == 0: print("None")
        else:
            for index, consumable_id in enumerate(self.consumables, start =1):
                print(f"{index}. {consumable_names[consumable_id]}", end = "   ")
                
            print()

    def clear_inventory(self):
        self.weapons.clear()
        self.armor.clear()
        self.consumables.clear()



