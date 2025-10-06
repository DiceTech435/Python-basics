from struct import *

# STRUCT -- Takes data in python and converts it to a byte form
# i -int
# f -float
data = pack("iif", 8, 9, 2.5)
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))
print(data)

real_data = unpack("iif", data)
print(real_data)


# MAP
number = [20, 50, 10, 30]
def double_number(people):
    return people * 2
map(double_number, number)
new_number = list(map(double_number, number))
print(new_number)
