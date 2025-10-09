# ITERABLE -- An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop


# LISTS
numbers = [1, 2, 3, 4, 5]
# TUPLES
numbers = (1, 2, 3, 4, 5)
for number in reversed(numbers):
    print(number, end="-")


# SETS
fruits = {"apple", "orange", "banana", "cocunut"}
for fruit in fruits:
    print(fruit)


# STRINGS
name = "Amevye Matthew"
for character in name:
    print(character, end=" ")


# DICTIONARIES
my_dictionary = {"A": 1, "B": 2, "C": 3}
# For keys
for key in my_dictionary:
    print(key)
# For values
for value in my_dictionary.values():
    print(value)
# For both key and value
for key, value in my_dictionary.items():
    print(f"{key} = {value}")