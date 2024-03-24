#main.py

#general ideas, character class with health, name, attack stat, armor stat? armor pen, weapon selection
#enemies with fixed names, health, attack, eg goblin has 5 health, 3 attack, whatever
#combat flow is just while character.is_alive() and enemy.is_alive():
#also needs to be character creation thing in beginning, all laid out in main


import util as u
from entity import *
from actions import Actions as a
from combat import *
import create_character
import map as map


def main():


    m = map.Map(10,10)
   # m.display()

    m.update(3,7)
    m.display()

    return

if __name__ == "__main__":
    main()
    