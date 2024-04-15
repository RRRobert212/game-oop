#map.py

from entity import *
from items import *
from combat import *
import os
import sys


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Map:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['.' for i in range(width)] for i in range(height)]
        self.walls = []



    #functions for spawning entities
    def place_entity(self, entity, x, y):
        """place an entity at a position given by coordinates x,y. Takes entity_id as input"""
        # Update the map to reflect the character's position (assuming character_x and character_y are the coordinates of the character)
        self.grid[y][x] = entity.get_first_letter() # Place the character symbol at the new position
        entity.set_pos(x, y)


    def redraw_entity(self, entity):
        """places the entity on the map at its position given by entity.get_pos_x/y"""
        self.grid[entity.get_pos_y()][entity.get_pos_x()] = entity.get_first_letter()

    def clear_entity_or_item(self, entity):
        """clears a specific entity from its position"""
        self.clear_xy(entity.get_pos_x(), entity.get_pos_y())


    #functions for spawning items
    def place_item(self, item, x, y):
        """place an item at a given position"""
        a = item.get_item_type()
        #prints the first letter of "weapon", "armor", etc on the map depending on item type.
        self.grid[y][x] = a[0]
        item.set_pos(x,y)


    
    
    #general display functions
    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        """prints the map"""
        for row in self.grid:
            print(' '.join(row))

    def clear_xy(self, x, y):
        """clears a position given the coordinates"""
        self.grid[y][x] = '.'

    def clear_all(self):
        """resets whole map to '.'s """
        self.grid = [['.' for i in range(self.width)] for i in range(self.height)]




#functions for entity movement
    def move(self, entity, dx, dy):
        """basically a utility function for directional movement functions"""
        #but I can also use it later if I want to make things move in different ways
        self.clear_entity_or_item(entity)

        #this should prevent wall clipping
        if not self.is_wall(entity.get_pos_x()+dx, entity.get_pos_y()+dy):
            entity.set_pos(entity.get_pos_x()+ dx, entity.get_pos_y() + dy)
        
        #this should prevent leaving map boundaries
        if entity.get_pos_x() <= 0:
            entity.set_pos(0, entity.get_pos_y())
        if entity.get_pos_y() <= 0:
            entity.set_pos(entity.get_pos_x(), 0)
        if entity.get_pos_y() >= self.height:
            entity.set_pos(entity.get_pos_x(), self.height-1)
        if entity.get_pos_x() >= self.width:
            entity.set_pos(self.width-1, entity.get_pos_y())
            print

        self.redraw_entity(entity)
        self.display() #do we want to make displaying the map a definite part of the move function??? maybe not but I'll keep it for now

    def move_left(self, entity):
        self.move(entity, -1, 0)

    def move_right(self, entity):
        self.move(entity, 1, 0)

    def move_up(self, entity):
        self.move(entity, 0, -1)

    def move_down(self, entity):
        self.move(entity, 0, 1)

    def movement_loop(self, character):
        i = input("WASD: ")

        if i == "w":
            self.move_up(character)
        elif i == "a":
            self.move_left(character)
        elif i == "s":
            self.move_down(character)
        elif i == "d":
            self.move_right(character)
        elif i == "x": return #exit input, for testing
        else: print("Invalid input.")



#functions to handle collisions    
    def collision_detection(self, entity_1, entity_2):
        """returns true if entity_1 and entity_2 are in the same position on the map"""
        if (entity_1.get_pos_x() == entity_2.get_pos_x() ) and (entity_1.get_pos_y() == entity_2.get_pos_y()):
            return True
        else: return False


    def combat_collision(self,character):
        """takes the character as input, checks if there is collision between character and any spawned enemies"""
        if len(spawned_enemies) == 0:
            return
        else:
            for enemy in spawned_enemies:
                if Map.collision_detection(self, character, enemy):
                    combat_flow(character, enemy)
                    if character.is_alive():
                        spawned_enemies.remove(enemy)




    def consumable_collision(self, character):
        if len(spawned_items) == 0:
            return
        else:
            for item in spawned_items:
                if Map.collision_detection(self, character, item):
                    if item.get_item_type() == "armor":
                        character.add_armor_to_inventory(item)

                    elif item.get_item_type() == "weapon":
                        character.add_weapon_to_inventory(item)

                    elif item.get_item_type() == "consumable":
                        character.add_consumable_to_inventory(item)

                    print()
                    print(f"{character.get_name()} obtained {item.get_name()}!")

                    spawned_items.remove(item)



    #walls
    def spawn_wall(self, x, y):
        """Place a wall at the given position"""
        self.grid[y][x] = '#'
        self.walls.append(Wall(x, y))

    def is_wall(self, x, y):
        """Check if a given position is a wall"""
        for wall in self.walls:
            if wall.x == x and wall.y == y:
                return True
        return False
    


