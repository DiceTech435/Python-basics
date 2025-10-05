# LISTS/ARRAY []

# names = ['Jonn', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'John'
# print(names[-1])
# print(names[2:4])
# print(names[2:])
# print(names[:3])
# print(names[:])
# # Note, if empty, it takes 0 as default

# # 2nd
# numbers = [3, 6, 2, 8, 4, 10]
# maximum = numbers[0]
# for number in numbers:
#     if number > maximum:
#         maximum = number
#         print(maximum)

# 3rd
numbers = [3, 6, 2, 8, 4, 10]
minimum = numbers[0]
for number in numbers:
    if number < minimum:
        minimum = number
        print(minimum)


# 2-DIMENSIONAL LISTS
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# matrix[0] = [3, 90, 11]
# print(matrix[0][1])
# for row in matrix:
#     for item in row:
#         print(item)


# # LIST FUNCTIONS/METHODS
numbers = [5, 2, 1, 5, 7, 4]
# Numbers/String Methods
    # .append() --adds to the last
    # .insert(index, object)
    # .remove(object)
    # .clear() ---removes all in a list
    # .pop() ---removes last item on the list
    # .sort() -- sorts in ascending order
    # .reverse() -- reverses in descending order
    # .copy() -- just helps print the initial without redefining
    # .choice()
    # .count()
    # .extend()
    # .split()

# # 1st
# numbers.append(20)
# numbers.insert(0, 10)
# numbers.remove(1, 4)
# numbers.clear()
# numbers.sort()
# numbers.reverse()
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers)
# print(numbers2)

# # Boolean Methods
    # .index()
    # .count()
    # .insert()
    # .copy()

# # 2nd
# print(numbers.index(5)) 
# print(50 in numbers) -- this doesnt return error
# print(numbers.count(5))


# EXAMPLES -- remove duplicated numbers
# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
#     print(uniques)