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