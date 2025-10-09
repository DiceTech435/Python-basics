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


# DATA TYPES/VARIABLES
    # str ""
        # format str f"" -- adding variables
            #age = f"{30} years old"
                    # print(age) 
        # r str r"" -- rescaping new line -- \ -escape sequence--ignore any quote and treat as a normal string
    # numbers
        # int -- 40, 3, 90
        # float -- 4.2, 49.1
    # bool


# FUNCTIONS
# TYPE CASTING FUNCTIONS -- type() -- get the variable/data type
    # str()
    # int()
        # birth_year = input('Birth year: ')
        # age = 2019 - int(birth_year)
        # print(age)
    # float()
    # bool()

# TASKS
    # print()
    # input() #always stored as a string, hence convert it to int or float
    # type()
    # help()
    # dir()
    # max

# For string
    # len(username) #gets the length of a string
        # course = 'Python for Beginners'
        # print(len(course))
    # reversed(range(1, 11))

# # Maths/numbers
    # round(x, 2)
    # abs(-3)
    # pow(3, 2)
    # max(x, y, z)
    # min(x, y, z)
    # range(10)
    # import math (math module)
        # math.pi
        # math.e
        # math.sqrt
        # math.ceil(2.9)
        # math.floor(2.9)

# For Files
    # open('shop.txt', 'w')
    # .write("We are writing a file in python")
    # .read()
    # .close()

# METHODS
    # For string -- print(help(str))
        # .upper()
        # .lower()
        # .capitalize() -- first char 
        # .title()
        # .find('p') -- first occurence of a character
        # .rfind('o') -- reverse/last occurence of a character
        # .count('-')
        # .replace('Boy', 'Girl')
    # Boolean String
        # .isdigit() -- true/false if all contains digits
        # .isalpha() -- true/false if all contains alphabets
        # .endswith()

    # For Lists/Dictionaries/Topols -- print(dir(iterable)), print(help(iterable))
        # .items() -- only work for strings in dictionaries
        # .count(self, x) --- 
        # .index(self, x, start, end)

# BOOLEAN KEYWORDS
    # in
        # course = 'Python for Beginners'
        # print('python' in course)
    # is / ==
    # not
    # break -- stop executing
    # continue
    # pass -- pass this line, don't worry about it instead of showing error
    # import
    # from ... import ...

# CONCATENATION
    # name = input("What is your name? ")
    # color = input("What color do you like? ")
    # print("Hi " + name + " you like " + color)

# FORMATTED STRING/placeholders
    # first = "John"
    # last = "Smith"
    # message = first '[' + last + '] is a coder'
    # msg = f'{first} [{last}] is a coder'

# TEMPLATE LITERALS
    # print(f"Hi {name}")
    # print(r"C:\Desktop\new")
    # print("The number is: ", num) 

# MULTI-LINE STRING
course = '''
    Hi John, 
    Here is our first email to you.

    Thank you, 
    The support team
'''

# STRING INDEXING / CHAR INDEX [start : end : step]
course = 'Python for beginners'
credit_number = "123-456-789-012-345"
print(course[-2])
print(course[0:3])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::2]) #count by 2
print(credit_number[::-1]) #reverse a string
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
# Note: 0 is default


# FORMAT SPECIFIERS == {value:flags}
# .(number)f round to a decimal point (fixed point)
# :(number) allocate that many spaces
# :03 allocate and zero pad that many spaces
# :< left justify
# :> right justify
# :^ center align
# :+ indicate positive value
# := leftmost position
# : insert a space before positive numbers
# :, comma seperator
    # price = 1200.34
    # print(f"Price is ${price:+,.2f}")

# OPERATORS
# Arithmetic +, - *, /, //, %, ^, **,
# Argumented assignment +=, -=, *=, 
# Opertaor precedence BODMAS
# Logical operators and, or, not
# Membership in, not in
# Identity is, is not
# Assignment =, +=, -=, *=, /=
# Comparison operators <, >, <=, >=, ==, ===, !=, !== (True/False)
# Indexing operator [start : end : step]
# Escape sequence \ -ignore any quote and treat as a normal string
# New line \n -- print("My name is\n Matthew")
# Ignore New line r"" --- print(r"C:\Desktop\new")



# # BITWISE
# Cryptography, networking, data compression, image processing, handware control/IoT, performance optimization
    # 0 = 0000
    # 1 = 0001
    # 2 = 0010
    # 3 = 0011
    # 4 = 0100
    # 5 = 0101
# OPERATORS/OPERATIIONS
# AND &, OR |, XOR ^, NOT ~, Left shift <<, Right shift >>
a = 50 #110010
b = 25 #011001
       #010000
c = a & b
print(c)

a = 240
y = a >> 2
print(y)
