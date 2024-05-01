#items.py

from constants import *

class Items:
    def __init__(self, item_id):
        self.name = self.get_name()
        self.item_id = item_id
        self.item_type = None
        self.pos_x = None
        self.pos_y = None

    def get_name(self):
        raise NotImplementedError("Subclasses must implement get_name method")
    
    def get_id(self):
        return self.item_id
    
    def display_name(self):
        print(self.get_name())

    def get_item_type(self):
        return self.item_type
    

    def get_pos_x(self):
        return self.pos_x
    def get_pos_y(self):
        return self.pos_y
    
    def set_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    
    @staticmethod
    def spawn_weapon(weapon_id):
        weapon = Weapon(weapon_id)
        spawned_items.append(weapon)
        return weapon

    @staticmethod
    def spawn_armor(armor_id):
        armor = Armor(armor_id)
        spawned_items.append(armor)
        return armor

    @staticmethod
    def spawn_consumable(consumable_id):
        consumable = Consumable(consumable_id)
        spawned_items.append(consumable)
        return consumable


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
    
class Consumable(Items):
    def __init__(self, consumable_id):
        self.consumable_id = consumable_id
        super().__init__(consumable_id)
        self.item_type = "consumable"
        self.effect_stat = self.get_effect_stat()

    def get_name(self):
        return consumable_names[self.consumable_id]
    
    def get_effect_stat(self):
        return consumbale_effect_factor[self.consumable_id]
    

