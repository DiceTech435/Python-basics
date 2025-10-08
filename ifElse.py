is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")   
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
    print(f"Down payment: ${down_payment}")


# weight = int(input('weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")


name = "Matthew"
if name is "Matthew":
    print("Welcome Matthew")
elif name is "Abraham":
    print("Welcome Abraham")
elif name is "Chinedu":
    print("Welcome Chinedu")
else:
    print("please register")


# TERNARY OPERATORS  
num = -5
a = 6
b= 7
age = 13
temperature = 30
user_role = "admin"

result = "Positive" if num > 0 else "Negative"
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited access"


print(result)
print(max_num)
print(min_num)
print(status)
print(status)
print(access_level)