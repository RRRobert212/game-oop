#items.py

from constants import *

class Items:
    def __init__(self, item_id):
        self.name = self.get_name()
        self.item_id = item_id
        self.item_type = None

    def get_name(self):
        raise NotImplementedError("Subclasses must implement get_name method")
    
    def get_id(self):
        return self.item_id
    
    def display_name(self):
        print(self.get_name())

    def get_item_type(self):
        return self.item_type


#weapons
class Weapon(Items):
    def __init__(self, weapon_id):
        self.weapon_id = weapon_id
        super().__init__(weapon_id)
        self.item_type = "weapon"
        self.attack_stat = self.get_attack_stat()

    def get_name(self):
        return weapon_names[self.weapon_id]

    def get_attack_stat(self):
        return weapon_damage_factor[self.weapon_id]




#armor
class Armor(Items):
    def __init__(self, armor_id):
        self.armor_id = armor_id
        super().__init__(armor_id)
        self.item_type = "armor"
        self.block_stat = self.get_block_stat()

    def get_name(self):
        return armor_names[self.armor_id]
    
    def get_block_stat(self):
        return armor_block_factor[self.armor_id]
    


w = Weapon(1)
a = Armor(0)

print(w.get_item_type())
print(a.get_item_type())