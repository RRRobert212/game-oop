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

        print("Weapons: ", end = '')
        if len(self.weapons) == 0: print("None.")
        else:
            for weapon in self.weapons:
                print(weapon[1] +". ", end = '')
            print()

        print("Armor: ", end ='')
        if len(self.armor) == 0: print("None")
        else:
            for armor in self.armor:
                print(armor[1] + ". ", end = '')
                print()

        print("Consumables: ", end = '')
        if len(self.consumables) == 0: print("None")
        else:
            for consumable in self.consumables:
                print(consumable[1]+ ". ", end = '')
                print()
        print()

    def add_armor(self, armor_id):
        """takes armor_id as input, append [armor id, armor name] to armor inventory"""
        self.armor.append([armor_id, armor_types[armor_id]])

    def add_consumbale(self, consumbale_id):
        """takes armor_id as input, append [armor id, armor name] to armor inventory"""
        self.consumable.append([consumbale_id, consumable_types[consumbale_id]])




