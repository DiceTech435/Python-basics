# MODULES --files with python codes with diifferent sections
import funcUtils
from funcUtils import emoji_converter
from funcUtils import square
# from lists import min
import CustomFuncs.shipping
from CustomFuncs.shipping import calc_shipping, cal_tax
CustomFuncs.shipping.calc_shipping()
import random 


funcUtils.greet_user("James", "Vivian", 26)
funcUtils.find_min([3, 6, 2, 8, 4, 10])
print(square(21))
# print(min)
calc_shipping

# Random number
for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

# Choice Leader
members = ["John", "Mary", "Bob", "Mosh"]
leader = random.choice(members)
print(leader)

# Roll Dice  
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return fisrt, second
    

# dice = Dice()
# print(dice.roll)
