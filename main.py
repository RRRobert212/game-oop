#main.py

#general ideas, character class with health, name, attack stat, armor stat? armor pen, weapon selection
#enemies with fixed names, health, attack, eg goblin has 5 health, 3 attack, whatever
#combat flow is just while character.is_alive() and enemy.is_alive():
#also needs to be character creation thing in beginning, all laid out in main


import util as u
from entity import *


def main():

    e = Enemy(0)
    e.attack_roll()
    e.health_roll()



    c = Character("Robert", 25, 2)
    c.attack_roll()
    c.health_roll()

    print("\n")
    print("Character name: " + str(c.get_name()))
    print("Age: " + str(c.get_age()))
    print("Race: " + str(c.get_race()))
    print("Attack: " + str(c.get_attack()))
    print("Health: " + str(c.get_health()))

    print("\n")

    print("Enemy attack: " + str(e.get_attack()))
    print("Enemy health: " + str(e.get_health()))
    print("Enemy race: " + str(e.get_race()))
    print("\n")



    return

if __name__ == "__main__":
    main()
    