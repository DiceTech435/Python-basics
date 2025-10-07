# EXTENSIONS 
# python by Microsoft
# python debugger by Microsoft
# pylance by Microsoft
# Jupyter (by Microsoft)
# Code Runner (by Jun Han)
# Black/Ruff/flake8 (for linting & formatting)
# GitLens (for version control)
# isort (Automatically sorts imports)
# Material Icon Theme (by Philip Kief)


# DATA TYPES
# str "" \ -escape sequence--ignore any quote and treat as a normal string
# numbers
    # int -- 40, 3, 90
    # float -- 4.2, 49.1
# bool

# BUILT-IN FUNCTIONS
# # For tasks
# print()
# input() #always otten as a string, hence convert to int or float
# max

# # For data type format
# str()
# int()
# float()
# bool()
# type()


# For File
# open('shop.txt', 'w')
# .write("We are writing a file in python")
# .read()
# .close()

# # For string
# len() #gets the length of a string

# # Maths/numbers
# round()
# abs()
# range(10)
# import math (math module)
# math.ceil(2.9)
# math.floor(2.9)


# METHODS
# For string
# .upper()
# .lower()
# .title()
# .find('p')
# .replace('Boy', 'Girl')


# For Lists/Dictionaries/Topols
# .items() -- only work for strings in dictionaries
# .count(self, x) --- 
# .index(self, x, start, end)

# BOOLEAN KEYWORDS
# in
# is or ==
# not
# break -- stop executing
# pass -- pass this line, don't worry about it instead of showing error
# continue
# import
# from ... import ...


# course = 'Python for Beginners'
# print('python' in course)


# CONCATENATION
# name = input("What is your name? ")
# color = input("What color do you like? ")
# print("Hi " + name + " you like " + color)

# TEMPLATE LITERALS
# print(f"Hi {name}")
# print(r"C:\Desktop\new")
# print("The number is: ", num)

# birth_year = input('Birth year: ')
# age = 2019 - int(birth_year)
# print(age) 

# MULTI-LINE STRING
course = '''
Hi John, 
Here is our first email to you.

Thank you, 
The support team
'''

# CHAR INDEX []
course = 'Python for beginners'
print(course[-2])
print(course[0:3])

# FORMATTED STRING/placeholders
# first = "John"
# last = "Smith"
# message = first '[' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'

# course = 'Python for Beginners'
# print(len(course))

# OPERATORS
# Arithmetic +, - *, /, //, %, ^, **,
# Argumented assignment +=, -=, *=, 
# Opertaor precedence BODMAS
# Logical operators and, or, not
# Comparison operators <, >, <=, >=, ==, ===, !=, !==
# Escape sequence \ -ignore any quote and treat as a normal string
# New line \n -- print("My name is\n Matthew")
# Ignore New line r"" --- print(r"C:\Desktop\new")


# # BITWISE OPERATORS
# &, >>,  
a = 50 #110010
b = 25 #011001
       #010000
c = a & b
print(c)

a = 240
y = a >> 2
print(y)