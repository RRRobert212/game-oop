#combat.py

from entity import *
from actions import Actions as a
import util as u

def combat_flow(character, opponent):
    in_combat = True
    """main combat flow for encounter between character and enemy"""
    print()
    print(f"{character.get_name()} has encountered a {opponent.get_name()}!")
    print()

    while in_combat:


        while True:

            print(f"{character.get_name()}'s turn!")

            print("What will you do? ")
            print("1. Attack                2. Special Move")
            print("3. Open Inventory        4. Run Away")

            try:
                choice = int(input("Enter your choice: "))
                print()

                if choice == 1:
                    attack_flow(character, opponent)
                    if not opponent.is_alive():
                        combat_end_victory(character, opponent)
                        in_combat = False
                    break

                elif choice == 2:
                    #special flow should be just like attack flow but with different move
                    #also it shouldn't always be (character, opponent) as args.
                    #or maybe it should, this gets weird and specific with move type
                    special_flow()
                    if not opponent.is_alive():
                        combat_end_victory(character, opponent)
                        in_combat = False
                    break


                elif choice == 3:
                    u.load_short()
                    character.inventory.display_inventory()
                    print()

                elif choice == 4:
                    u.load_short()
                    x = dice_6()
                    if x >= 3:
                        combat_end_run(character, opponent)
                        in_combat = False
                        break
                    else: 
                        print("You failed to escape! ")
                        break


                else: print("Please enter a valid choice from the options!")

            except ValueError: print("Please enter an integer to make your choice!")

        if not in_combat: continue

        load_short()

        #enemy actions, this is hard cause I basically have to design an AI for now though, they'll just punch
        #note that for an attack to be possible, the enemy needs at least 1 weapon in their inventory. Most enemies will have punch
        print(f"{opponent.get_name()}'s turn!")
        load_short()

        a.attack(opponent, character, 0)
        load_short()
        if not character.is_alive():
            combat_end_defeated(character, opponent)
            in_combat = False

    print("Encounter over.")


def attack_flow(attacker, victim):
    print("What weapon will you use?")
    attacker.inventory.display_weapons()

    while True:

        choice = int(input("Enter your choice: "))
        u.load_short()

        try:
            if 0 < choice <= len(attacker.inventory.weapons):
                chosen_weapon_id = attacker.inventory.weapons[choice-1][0]
                print()
                break    
                
        except ValueError:
            print()

    a.attack(attacker, victim, chosen_weapon_id)

def special_flow():
    print("You don't have any special moves, idiot.")
    
def combat_end_run(runner, opponent):
    print(f"{runner.get_name()} ran away from {opponent.get_name()} safely!" )

def combat_end_victory(victor, opponent):
    print(f"{victor.get_name()} defeated {opponent.get_name()}!")

def combat_end_defeated(loser, opponent):
    print(f"{opponent.get_name()} defeated {loser.get_name()}. You died!")
