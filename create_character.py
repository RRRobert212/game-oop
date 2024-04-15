#create character.py

from entity import *
from util import *

def create_character():
    """basic character creation, prompts user for name, age, and race selection. automatically roles for stats with fake loading icons"""
    print("Welcome to the character creation!")
    c = Character("NULL", -1, -1)
    

    c.update_name(input("Enter your name: "))

    try: c.update_age(int(input("Enter your age: ")))

    except ValueError: pass

    if c.get_age() > 120:
        print(f"Okay, let's be reasonable, you can't be {c.get_age()} years old.")
        c.update_age(-1)

    while c.get_age() <= 0:
        try: c.update_age(int(input("Please enter a valid positive integer for your age: ")))

        except ValueError: pass


        if c.get_age() > 120:
            print(f"Okay, let's be reasonable, you can't be {c.get_age()} years old.")
            c.update_age(-1)

    print("Choose your race: ")
    i = 0
    for race in race_list:
        i += 1
        print(f"{i}: {race}")

    while True:
        try:
            choice = int(input("Please enter the integer corresponding to your chosen race: ")) - 1
            if choice < 0 or choice >= len(race_list):
                print("Invalid choice. Please enter a valid integer within the range.")
            else:
                c.update_race(choice)
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


    print(f"Name: {c.get_name()} \nAge: {c.get_age()} \nRace: {c.get_race()}")

    print("Rolling for your health", end = "") 
    load_short()
    c.health_roll()
    print(f"\nHealth: {c.get_health()}")
    print("Rolling for your attack", end = "")
    load_short()
    c.attack_roll()
    print(f"\nAttack: {c.get_attack()}")

    
    #adds fists as a default weapon
    c.inventory.clear_inventory()
    c.inventory.add_weapon(0)




    return c




