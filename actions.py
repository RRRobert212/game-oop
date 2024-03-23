#actions.py


#I want an attack function that both characters and enemies can use
#I also want this class to encapsulate actions in general so I can add like a heal action and other stuff
#I guess it has two inputs, the user (with their attack stat)
#and the target (with their health stat)
from entity import *

class Actions:

    @staticmethod
    def receive_damage(target, amount): #can modify this so it can heal also actually don't cause of the print statement
        """generic function to deal damage to target. Takes target, and amount of damage. Outputs damage and remaining health"""
        target.set_health(target.get_health() - amount)
        if target.is_alive():
            print(str(target.get_name()) + " received " + str(amount) + " damage! They have " + str(target.get_health()) + " health remaining.")
        else: print(f"{target.get_name()} reveived {amount} damage! They have no health remaining!")

    @staticmethod
    def punch(user, target): 
        print(str(user.get_name()) + " used punch! ")
        Actions.receive_damage(target, user.get_attack())
        if user.get_attack() > 40:
            print(str(target.get_name()) + " pooped because that was such a hard punch")

    @staticmethod
    def heal_damage(target, amount):
        """heals target health by given amount, target and amount as input, prints statement about it"""
        target.set_health(target.get_health() + amount)
        print(str(target.get_name()) + " healed for " + str(amount) + " health! They now have " + str(target.get_health()) + " health.")

