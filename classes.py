# CLASSES -- templates/blueprint for creating objects
# using Pascal 
# Magic methods
# Objects ---actual instanses based on the class created

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


# Inheriatnce, Multiple Inheritance
# DRY--Don't repeat Yourself
class James(Person):
     pass 

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