#combat.py

from entity import *
from actions import Actions as a

def combat_flow(character, opponent):
    """main combat flow for encounter between character and enemy"""

    print(f"{character.get_name()} has encountered a {opponent.get_name()}!")

    while character.is_alive() and opponent.is_alive():

        input("Press enter to punch!")
        a.punch(character, opponent)

        if not opponent.is_alive():
            print(f"{opponent.get_name()} has been defeated!")
            break

        print(f"{opponent.get_name()}'s turn!")
        a.punch(opponent, character)

        if not character.is_alive():
            print(f"{opponent.get_name()} defeated {character.get_name()}! You lose!")
            break
    print("Combat ends.")

