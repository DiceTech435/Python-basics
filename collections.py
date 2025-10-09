# COLLECTIONS -- single "variable" used to store multiple values
    # List = [] ordered and changeable. Duplicates OK
    # Set = {} unordered and immutable, but Add/Remove Ok. No duplicates
    # Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# FUNCTIONS
    # print(dir(iterable))
    # print(help(iterable))
    # print(len(iterable))
    # in -- Boolean
        # print("apple" in fruits)


# LISTS
fruits = ["apple", "orange", "banana", "coconut"]
fruits[0] = "pineapple"
print(fruits[::2])
print(fruits[::-1])
for fruit in fruits:
    print (fruit)

# List's methods -- print(help(list))
    # .append() --adds to the last
    # .insert(index, object)
    # .remove(object)
    # .clear() ---removes all in a list
    # .pop() ---removes last item on the list
    # .sort() -- sorts in ascending alphabetical order
    # .reverse() -- reverses in descending order
    # .index("")
    # .copy() -- just helps print the initial without redefining
    # .choice()
    # .count() -- for list because duplicates are OK
    # .extend()
    # .split()


# SETS -- same as lists but an item cannot appear twice
shop = {"Milk", "Garri", "Sugar", "Tea", "Cream", "Garri"}
if "Milk" in shop:
    print("Yes you have Milk in the shop")
else:
    print("You need milk")

# Set's methods -- print(help(set))
    # .add("")
    # .remove()
    # .pop()
    # .clear()


# TUPLE()-- Operate/same to lists, but inmutable, unchnageable, unmodifiable, FASTER
coordinates = (1, 2, 3)

# # method 1
# x = coordinates[0]
# x = coordinates[1]
# z = coordinates[2]

# method 2
# BY UNPACKING ARGUMENTS
x, y, z = coordinates
print(y)

# Methods of Tuple -- print(help(tuple))
    # .count(self, x) --- 
    # .index(self, x, start, end)





# 2-DIMENSIONAL COLLECTIONS
# Lists
# 1st
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# 2nd
groceries = [
    ["apple", "orange", "banana", "coconut"],
    ["celery", "carrots", "potatoes"],
    ["chicken", "fish", "turkey"]
]

for collections in groceries:
    for food in collections:
        print(food, end=" ")
    print()


# Sets
groceries = [
    {"apple", "orange", "banana", "coconut"},
    {"celery", "carrots", "potatoes"},
    {"chicken", "fish", "turkey"}
]

# Tuple
groceries = [
    ("apple", "orange", "banana", "coconut"),
    ("celery", "carrots", "potatoes"),
    ("chicken", "fish", "turkey")
]

# Nested Tuple
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()