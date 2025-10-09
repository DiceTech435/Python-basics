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






# <=================LIST COMPREHENSION=================>
# A concise way to create lists. Compact and easier to read than traditional loops. 
# [expression for value in iterable if condition]

# For Numbers Without conditions
# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)

# print(doubles)

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]
print(doubles)
print(triples)
print(squares)

# For Numbers With conditions
numbers = [1, -2, 3, -4, 5, -6, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(positive_nums)
print(positive_nums)
print(even_nums)
print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)

# For strings without conditions
fruits = ["apple", "orange", "banana", "cocunut"]
fruits = [fruit.upper() for fruit in fruits]
fruits_chars = [fruit[0] for fruit in fruits]
print(fruits)
print(fruits_chars)
