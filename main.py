#main.py

import util as u
from entity import *
from actions import Actions as a
from combat import *
import create_character
import map as map


def main():

    c = create_character.create_character()
    e = Enemy.spawn_ghoul() #probably update the spawn function so it automatically puts them on the map with spawn_entity
    #but if I want to do that I prob have to add the map as a parameter to the spawn function

    m = map.Map(30,30)
   # m.display()
    m.spawn_entity(c, 7,4)
    m.spawn_entity(e, 2,2)

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


        
        #this is collision detection, it needs to be much better than this
        #I think I have to append all enemy and character positions in a list when they spawn
        #and then I constantly run collision detection between the character, and the positions in the list
        #this will also work for collisions with objects like walls. I just need a slightly different function
        #like the character to enemy collision detection initiates combat
        #but character to wall blocks movement in one direction
        #and character to collectible does something else
        if (c.get_pos_x() == e.get_pos_x() ) and (c.get_pos_y() == e.get_pos_y()):
            combat_flow(c,e)
            m.display()
            
        





    return

if __name__ == "__main__":
    main()
    