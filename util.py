#util.py

import random
import time
from constants import *

def dice_6():
    r = random.randint(1,6)
    return r

def load_short():
    """prints 3 dots with pauses, a sort of loading screen"""
    for i in range(3):
        time.sleep(0.25)
        print(".", end = '', flush= True)
    time.sleep(0.25)
    print()

def stat_roll(stat_range):
    """Simplifies rolling for stats within classes"""

    return random.randint(stat_range[0],stat_range[1])


def weapon_damage_roll(weapon_id_number):
    """utility function that returns random float in weapons damage factor range"""
    return random.uniform(weapon_damage_factor[weapon_id_number][0], weapon_damage_factor[weapon_id_number][1])

