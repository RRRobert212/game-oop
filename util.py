#util.py

import random
import time

def dice_6():
    r = random.randint(1,6)
    return r

def load_short():
    for i in range(3):
        time.sleep(0.25)
        print(".", end = '', flush= True)
    time.sleep(0.25)

def stat_roll(stat_range):
    """Simplifies rolling for stats within classes"""

    return random.randint(stat_range[0],stat_range[1])

    