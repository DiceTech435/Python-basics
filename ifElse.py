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


# CONDITIONAL EXPRESSIONS/TERNARY OPERATORS  
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



# MATCH-CASE STATEMENT (switch) -- An alternative of using many 'elif' statements. For a cleaner and more readable syntax

def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _: #Wild card
            return "Not a valid day"

print(day_of_week(1))


# def is_weekend(day):
#     match day:
#         case "Sunday":
#             return True
#         case "Monday":
#             return False
#         case "Tuesday":
#             return False
#         case "Wednesday":
#             return False
#         case "Thursday":
#             return False
#         case "Friday":
#             return False
#         case "Saturday":
#             return True
#         case _: #Wild card
#             return False

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _: #Wild card
            return False

print(is_weekend("Saturday"))