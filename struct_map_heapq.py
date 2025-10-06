from struct import *
import heapq

# STRUCT -- Takes data in python and converts it to a byte form
# i -int
# f -float
data = pack("iif", 8, 9, 2.5)
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))
print(data)

# real_data = unpack("iif", "\x08\x00\x00\x00\t\x00\x00\x00\x00\x00 @")
real_data = unpack("iif", data)
print(real_data)


# MAP
number = [20, 50, 10, 30]
def double_number(people):
    return people * 2
map(double_number, number)
new_number = list(map(double_number, number))
print(new_number)



# HEAPQ
#  key=lambda
scores = [32, 45, 76, 34, 45, 50, 65]
print(heapq.nlargest(3, scores))
print(heapq.nsmallest(3, scores))

stocks = [
    {"ticker": "AAPL", "price": 204},
    {"ticker": "Shell", "price": 294},
    {"ticker": "BUA", "price": 23},
    {"ticker": "DG", "price": 78}
]

print(heapq.nsmallest(2, stocks, key=lambda stock:["price"]))

