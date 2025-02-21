#main.py

import util as u
from entity import *
from actions import Actions as a
from combat import *
import create_character
from map import *
from items import *


def main():

    curses.wrapper(play_test)




    return





def play_test(stdscr):
        
        curses.curs_set(0)
        m = Map(10, 10)
        spawned_enemies.clear()
        spawned_items.clear()


        c = Character("R",7,2)
        c.health_roll()
        c.attack_roll()


        enemy_1 = Enemy.spawn_enemy(0)
        enemy_2 = Enemy.spawn_enemy(1)
        r = Enemy.spawn_enemy(1)

        m.place_entity(enemy_1, 8, 2)
        m.place_entity(enemy_2, 2, 3)
        m.place_entity(r, 0,3)
        m.place_entity(c, 5, 5)

        weapon_1 = Items.spawn_weapon(2)
        weapon_2 = Items.spawn_weapon(1)

        armor_1 = Items.spawn_armor(0)

        m.place_item(weapon_1, 1, 7)
        m.place_item(weapon_2, 3, 3)
        m.place_item(armor_1, 9, 6)

        m.spawn_wall(0, 0)
        m.spawn_wall(0, 1)
        m.spawn_wall(0, 2)
        m.spawn_wall(6, 6)
        m.spawn_wall(7, 6)
        m.spawn_wall(8, 6)
        m.spawn_wall(8, 7)
        m.spawn_wall(8, 8)
        for item in spawned_items:
            stdscr.addstr(f"Item at ({item.get_pos_x()}, {item.get_pos_y()})")
        for enemy in spawned_enemies:
            print(f"Enemy at ({enemy.get_pos_x()}, {enemy.get_pos_y()})")
        while True:
            m.combat_collision(c)
            m.consumable_collision(c)

            m.display(stdscr)  # Render the map
            m.movement_loop(stdscr, c)


            if not c.is_alive():
                print("YOU LOSE!")
                choice = input("Do you want to play again? (Y/N): ").lower()
                if choice == "y":
                    break  # Break out of the current game loop and start again
                else:
                    return  # Exit play_test function, effectively ending the game




if __name__ == "__main__":
    main()
    