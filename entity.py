#entity.py

from util import *
from constants import *

class Entity: #a class for creatures with health and attack
    def __init__(self, health_range, attack_range):
        self.health = None
        self.attack = None
        self.health_range = health_range
        self.attack_range = attack_range
        self.race = None

    def health_roll(self):
        self.health = stat_roll(self.health_range)

    def attack_roll(self):
        self.attack = stat_roll(self.attack_range)

    def set_health(self, new_health):
        self.health = new_health

    def get_health(self):
        return self.health
    def get_attack(self):
        return self.attack
    def get_race(self):
        return self.race
    def get_name(self):
        return self.name
    
    
    def is_alive(self):
        if self.health > 0:
            return True
        else: return False

#a class for player characters, a race must be selected from the race list. characters have names and ages
class Character(Entity):
    def __init__(self, name, age, race_num):
        super().__init__(race_health[race_num], race_attack[race_num])
        self.name = name
        self.age = age
        self.race = race_list[race_num]

    def get_age(self):
        return self.age

#a class for enemies, they don't have ages, their names are just their race. a race must be selected from enemy list
class Enemy(Entity):
    def __init__(self, enemy_num):
        super().__init__(enemy_health[enemy_num], enemy_attack[enemy_num])
        self.enemy_num = enemy_num
        self.name = enemy_list[enemy_num]
        self.race = enemy_list[enemy_num]

    