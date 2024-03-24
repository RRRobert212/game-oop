#map.py

class Map:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['.' for i in range(width)] for i in range(height)]

    def display(self):
        for row in self.grid:
            print(' '.join(row))

    def update(self, character_x, character_y):
        # Update the map to reflect the character's position (assuming character_x and character_y are the coordinates of the character)
        self.clear_character()  # Clear the previous position of the character
        self.grid[character_y][character_x] = 'C'  # Place the character symbol at the new position
    
    def clear_character(self):
        # Clear the previous position of the character
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 'C':
                    self.grid[row][col] = '.'
                    return 