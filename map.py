#map.py

from entity import *
from items import *
from combat import *
import curses


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_pos_x(self):
        return self.x
    
    def get_pos_y(self):
        return self.y

class Map:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['.' for i in range(width)] for i in range(height)]
        self.walls = []
        self.items = spawned_items
        self.enemies = spawned_enemies
        self.character = spawned_character
        

    def render(self, stdscr):
        """Render the grid using curses."""
        stdscr.clear()
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                stdscr.addch(y, x, char)
        stdscr.refresh()

        

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
    def display(self, stdscr):
        """Display the map using curses."""
        stdscr.clear()
        for y, row in enumerate(self.grid):
            stdscr.addstr(y, 0, ' '.join(row))  # Add each row of the grid to the screen
        stdscr.refresh()

    def clear_xy(self, x, y):
        """clears a position given the coordinates"""
        self.grid[y][x] = '.'

    def clear_all(self):
        """resets whole map to '.'s """
        self.grid = [['.' for i in range(self.width)] for i in range(self.height)]




    def move(self, stdscr, entity, dx, dy):
        """Utility function for directional movement."""
        self.clear_entity_or_item(entity)

        # Prevent wall clipping
        if not self.is_wall(entity.get_pos_x() + dx, entity.get_pos_y() + dy):
            entity.set_pos(entity.get_pos_x() + dx, entity.get_pos_y() + dy)

        # Prevent leaving map boundaries
        if entity.get_pos_x() < 0:
            self.generate_line("W")
        elif entity.get_pos_x() >= self.width:
            self.generate_line("E")
        if entity.get_pos_y() < 0:
            self.generate_line("N")
        elif entity.get_pos_y() >= self.height:
            self.generate_line("S")

        self.redraw_entity(entity)
        self.display(stdscr)

    def move_left(self, stdscr, entity):
        self.move(stdscr, entity, -1, 0)

    def move_right(self, stdscr, entity):
        self.move(stdscr, entity, 1, 0)

    def move_up(self, stdscr, entity):
        self.move(stdscr, entity, 0, -1)

    def move_down(self, stdscr, entity):
        self.move(stdscr, entity, 0, 1)

    def is_wall(self, x, y):
        """Check if a position is a wall."""
        return any(wall.x == x and wall.y == y for wall in self.walls)

    def spawn_wall(self, x, y):
        """Add a wall to the grid."""
        self.grid[y][x] = '#'
        self.walls.append(Wall(x, y))

    def movement_loop(self, stdscr, character):
        """Loop to handle player movement."""
        while True:
            key = stdscr.getkey()

            if key == "w":
                self.move_up(stdscr, character)
            elif key == "a":
                self.move_left(stdscr, character)
            elif key == "s":
                self.move_down(stdscr, character)
            elif key == "d":
                self.move_right(stdscr, character)
            elif key == "x":
                return  # Exit the movement loop
            else:
                stdscr.addstr(self.height + 1, 0, "Invalid input.")
                stdscr.refresh()
            self.combat_collision(character)
            self.consumable_collision(character)




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
    
    def generate_line(self, NESW):
        """
        Generates a new row/column to append to the map on the north, east, south, or west side.
        NESW is a string and can be one of 'N', 'E', 'S', 'W' representing North, East, South, and West respectively.
        """
        if NESW == 'N':  # North
            new_row = ['.' for _ in range(self.width)]
            self.grid.insert(0, new_row)  # Add the new row at the top
            self.height += 1  # Since we added a row, increase the height

            for entity in self.enemies:
                entity.set_pos(entity.get_pos_x(), entity.get_pos_y() + 1)
            for item in self.items:
                item.set_pos(item.get_pos_x(), item.get_pos_y() + 1)
            for wall in self.walls:
                wall.y += 1
            for character in self.character:
                character.set_pos(character.get_pos_x(), character.get_pos_y() +1)
            
        elif NESW == 'E':  # East
            for row in self.grid:
                row.append('.')  # Add a new column element to the right of each row
            self.width += 1  # Since we added a column, increase the width
            
        elif NESW == 'S':  # South
            new_row = ['.' for _ in range(self.width)]
            self.grid.append(new_row)  # Add the new row at the bottom
            self.height += 1  # Since we added a row, increase the height
            
        elif NESW == 'W':  # West
            for row in self.grid:
                row.insert(0, '.')
            self.width += 1
            # Update x-coordinate of all entities, items, and walls
            for entity in self.enemies:
                entity.set_pos(entity.get_pos_x() + 1, entity.get_pos_y())
            for item in self.items:
                item.set_pos(item.get_pos_x() + 1, item.get_pos_y())
            for wall in self.walls:
                wall.x += 1
            for character in self.character:
                character.set_pos(character.get_pos_x()+1, character.get_pos_y())

        else:
            print("Invalid direction. Please choose 'N', 'E', 'S', or 'W'.")

