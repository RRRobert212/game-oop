#map.py

from entity import *


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

    def display(self):
        """prints the map"""
        for row in self.grid:
            print(' '.join(row))

    def spawn_entity(self, entity, x, y):
        """place an entity at a position given by coordinates x,y"""
        # Update the map to reflect the character's position (assuming character_x and character_y are the coordinates of the character)
        self.grid[y][x] = entity.get_first_letter() # Place the character symbol at the new position
        entity.set_pos(x, y)

    def respawn_entity(self, entity):
        """places the entity on the map at its position given by entity.get_pos_x/y"""
        self.grid[entity.get_pos_y()][entity.get_pos_x()] = entity.get_first_letter()
    
    def clear_xy(self, x, y):
        """clears a position given the coordinates"""
        self.grid[y][x] = '.'

    def clear_entity(self, entity):
        """clears an entity from a position"""
        self.clear_xy(entity.get_pos_x(), entity.get_pos_y())

    def clear_all(self):
        """resets whole map to '.'s """
        self.grid = [['.' for i in range(self.width)] for i in range(self.height)]

    def move(self, entity, dx, dy):
        """basically a utility function for directional movement functions"""
        #but I can also use it later if I want to make things move in different ways
        self.clear_entity(entity)

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

        self.respawn_entity(entity)
        self.display() #do we want to make displaying the map a definite part of the move function??? maybe not but I'll keep it for now

    def move_left(self, entity):
        self.move(entity, -1, 0)

    def move_right(self, entity):
        self.move(entity, 1, 0)

    def move_up(self, entity):
        self.move(entity, 0, -1)

    def move_down(self, entity):
        self.move(entity, 0, 1)


    
    def collision_detection(self, entity_1, entity_2):
        """returns true if entity_1 and entity_2 are in the same position on the map"""
        if (entity_1.get_pos_x() == entity_2.get_pos_x() ) and (entity_1.get_pos_y() == entity_2.get_pos_y()):
            return True
        else: return False



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
    



        