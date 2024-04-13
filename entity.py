#entity.py

from util import *
from constants import *
import map
from inventory import *

class Entity: #a class for creatures with health and attack
    def __init__(self, health_range, attack_range):
        self.health = None
        self.attack = None
        self.health_range = health_range
        self.attack_range = attack_range
        self.race = None
        self.pos_x = None
        self.pos_y = None
        self.inventory = Inventory()

    def health_roll(self):
        self.health = stat_roll(self.health_range)

    def attack_roll(self):
        self.attack = stat_roll(self.attack_range)

    def set_health(self, new_health):
        self.health = new_health

    #getter functions
    def get_health(self):
        return self.health
    def get_attack(self):
        return self.attack
    def get_race(self):
        return self.race
    def get_name(self):
        return self.name
    def get_pos_x(self):
        return self.pos_x
    def get_pos_y(self):
        return self.pos_y
    def get_first_letter(self):
        return self.get_name()[0].upper() 
    
    #update functions
    def update_name(self, new_name):
        self.name = new_name
    def update_race(self, new_race_num):

        self.race_num = new_race_num
        self.race = race_list[new_race_num]
    
    
    def is_alive(self):
        if self.health > 0:
            return True
        else: return False

    def set_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y


    #inventory functions (these already exist in the inventory class but this lets you add them by just referencing the item object, not the item id)
    def add_weapon_to_inventory(self, weapon):
        """adds weapon object to entity inventory"""
        self.inventory.add_weapon(weapon.get_id())

    def add_armor_to_inventory(self, armor):
        """adds armor object to entity inventory"""
        self.inventory.add_armor(armor.get_id())

    def add_consumable_to_inventory(self, consumable):
        """adds consumable object to entity inventory"""
        self.inventory.add_consumbale(consumable.get_id())

    

#a class for player characters, a race must be selected from the race list. characters have names and ages
class Character(Entity):
    def __init__(self, name, age, race_num):
        super().__init__(race_health[race_num], race_attack[race_num])
        self.name = name
        self.age = age
        self.race = race_list[race_num]
        self.race_num = race_num

    def get_age(self):
        return self.age
    def update_age(self, new_age):
        self.age = new_age

#a class for enemies, they don't have ages, their names are just their race. a race must be selected from enemy list
class Enemy(Entity):
    def __init__(self, enemy_num):
        super().__init__(enemy_health[enemy_num], enemy_attack[enemy_num])
        self.enemy_num = enemy_num
        self.name = enemy_list[enemy_num]
        self.race = enemy_list[enemy_num]

    
    #so these are obviously repetitive, I could just make a spawn function, but I like that they get different names, it makes calling them more intuitive
    #and I don't have to remember which enemy has which enemy number
    @staticmethod
    def spawn_goblin():
        e = Enemy(0)
        e.health_roll()
        e.attack_roll()
        return e
    
    @staticmethod
    def spawn_ghoul():
        e = Enemy(1)
        e.health_roll()
        e.attack_roll()
        return e
    


    