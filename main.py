#main.py

import util as u
from entity import *
from actions import Actions as a
from combat import *
import create_character
import map as map


def main():

    c = Character("Robert", 23, 1)
    c.health_roll()
    c.attack_roll()
    e = Enemy.spawn_ghoul() #probably update the spawn function so it automatically puts them on the map with spawn_entity
    #but if I want to do that I prob have to add the map as a parameter to the spawn function

    m = map.Map(10,10)
   # m.display()
    m.spawn_entity(c, 7,4)
    m.spawn_entity(e, 2,2)

    m.spawn_wall(3,3)
    m.spawn_wall(3,4)
    m.spawn_wall(3,5)

    m.spawn_wall(0,0)
    m.spawn_wall(9,9)

    m.display()


    
    #this eventually needs to get written as a function on its own, basically the whole gameplay
    while True:

        i = input("WASD: ")
        print("\n\n\n\n\n\n\n")

        if i == "w":
            m.move_up(c)
        elif i == "a":
            m.move_left(c)
        elif i == "s":
            m.move_down(c)
        elif i == "d":
            m.move_right(c)
        elif i == "x": return #exit input, for testing
        else: print("Invalid input.")


        
        if m.collision_detection(c,e):
            combat_flow(c,e)
            m.display()
            
        





    return

if __name__ == "__main__":
    main()
    