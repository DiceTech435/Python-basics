# CLASSES -- templates/blueprint for creating objects
    # using Pascal case in defining a class
    # Magic methods
    # Objects ---actual instanses based on the class created

# STEPS
    # Create a user module
    # Define a User class inside it
    # Add some helper functions if needed
    # Or wrap inside your own functions or classes to make your app's logic clean and reusable.

# 1st
class Point:

    # Properties
    # x = 2
    # y = 3

    # Connstruct/init function
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Methods
    def move(self):
        print("move")

    def draw(self):
        print('draw')


point1 = Point(5, 10)
# point1.draw()
point1.x = 8
print(point1.x)
print(point1.y)


# 2nd
class Person:

    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f'Hi, i am {self.name}!.')


john = Person("John Smith")
john.talk()

bob = Person("Bob James")
bob.talk()


# Inheriatnce
# DRY--Don't repeat Yourself
class James(Person):
     pass 
# Multiple Inheritance
class Esther(Person, Point):
     pass
 
name = "Tanko" 
 
# Overwrite
def talk(self):
    print(f'Hi, i am {name}!.')


james = James("James")
james.talk()

esther = Esther("Esther")
esther.talk()