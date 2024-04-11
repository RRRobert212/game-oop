#actions.py


#I want an attack function that both characters and enemies can use
#I also want this class to encapsulate actions in general so I can add like a heal action and other stuff
#I guess it has two inputs, the user (with their attack stat)
#and the target (with their health stat)
from entity import *
from constants import *

class Actions:

    @staticmethod
    def receive_damage(target, amount):
        """generic function to deal damage to target. Takes target, and amount of damage. Outputs damage and remaining health"""
        target.set_health(target.get_health() - amount)
        if target.is_alive():
            print(str(target.get_name()) + " received " + str(amount) + " damage! They have " + str(target.get_health()) + " health remaining.")
        else: print(f"{target.get_name()} reveived {amount} damage! They have no health remaining!")
        print()
        


    @staticmethod
    def attack(user, target, weapon_id): 
        """generic weak attack function, user argument punches target argument"""
        print(str(user.get_name()) + " attacked " + str(target.get_name() +" with their " + str(weapon_types[weapon_id])))

        damage = round(weapon_damage_roll(weapon_id) * user.get_attack())

        Actions.receive_damage(target, damage)


    @staticmethod
    def heal_damage(target, amount):
        """heals target health by given amount, target and amount as input, prints statement about it"""
        target.set_health(target.get_health() + amount)
        print(str(target.get_name()) + " healed for " + str(amount) + " health! They now have " + str(target.get_health()) + " health.")



