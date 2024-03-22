class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=' ')
    print()

def main():
    # Creating a list of student objects
    students = [
        Student("Alice", 20),
        Student("Bob", 22),
        Student("Charlie", 21)
    ]

    # Greeting each student
    for student in students:
        student.greet()

    # Printing numbers from 1 to 10
    print_numbers(10)

if __name__ == "__main__":
    main()



#MODULARIZED VERSION:
    

#student.py
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

#utils.py
        
def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=' ')
    print()

#main.py
    
from student import Student
from utils import print_numbers

def main():
    # Creating a list of student objects
    students = [
        Student("Alice", 20),
        Student("Bob", 22),
        Student("Charlie", 21)
    ]

    # Greeting each student
    for student in students:
        student.greet()

    # Printing numbers from 1 to 10
    print_numbers(10)

if __name__ == "__main__":
    main()


#lists
    # Example:
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#exceptions/error handling

# Example:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
else:
    print("Result:", result)
finally:
    print("Execution completed.")


#file I/O
# Example (reading from a file):
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)

# Example (writing to a file):
with open('file.txt', 'w') as f:
    f.write('Hello, World!')


#dictionaries

# Empty dictionary
my_dict = {}
# Dictionary with initial values
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing value by key
print(my_dict['name'])  # Output: Alice
# Using get() method (handles key absence gracefully)
print(my_dict.get('age'))  # Output: 30

# Adding a new key-value pair
my_dict['gender'] = 'Female'
# Modifying an existing value
my_dict['age'] = 31

# Using del keyword
del my_dict['city']
# Using pop() method (returns the value and removes the entry)
removed_value = my_dict.pop('age')

# Iterating over keys
for key in my_dict:
    print(key, my_dict[key])
# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)

# Check if key exists
if 'name' in my_dict:
    print("Key 'name' exists.")
# Get all keys
keys = my_dict.keys()
# Get all values
values = my_dict.values()
# Get number of key-value pairs
size = len(my_dict)
# Clear the dictionary
my_dict.clear()



#more class stuff

class Car:
    def __init__(self, make, model, year):
        self.make = make          # Public attribute
        self.model = model        # Public attribute
        self.__year = year        # Private attribute

    def get_year(self):
        return self.__year       # Getter method for private attribute

    def set_year(self, year):
        if year > 0:
            self.__year = year   # Setter method for private attribute
        else:
            print("Invalid year. Year must be greater than 0.")


# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Accessing public attributes
print("Make:", my_car.make)    # Output: Toyota
print("Model:", my_car.model)  # Output: Camry

# Accessing private attribute using getter method
print("Year:", my_car.get_year())  # Output: 2020

# Trying to access private attribute directly (will result in an AttributeError)
# print("Year:", my_car.__year)

# Modifying private attribute using setter method
my_car.set_year(2022)

# Accessing private attribute using getter method after modification
print("Modified Year:", my_car.get_year())  # Output: 2022

# Trying to set an invalid year
my_car.set_year(-1)  # Output: Invalid year. Year must be greater than 0.




#INTERACTION BETWEEN CLASSES 

class Player:
    def __init__(self, name):
        self.name = name

    def join_game(self, game):
        game.add_player(self)
        print(f"{self.name} has joined the game.")

    def leave_game(self, game):
        game.remove_player(self)
        print(f"{self.name} has left the game.")


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def list_players(self):
        print("Players in the game:")
        for player in self.players:
            print(player.name)


# Usage:
player1 = Player("Alice")
player2 = Player("Bob")
player3 = Player("Charlie")

game = Game()

player1.join_game(game)
player2.join_game(game)
player3.join_game(game)

game.list_players()

player2.leave_game(game)

game.list_players()
