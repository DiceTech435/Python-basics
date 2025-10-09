# FUNCTIONS def -- reusable block of code
# Paramters -- placeholders for recieving informations on a defined function
# Arguments -- value supplied to a function. Must match with the set of parameters

# TYPES OF FUNCTIONS Hierarchycally
# Positional arguments
# Default arguments
# Keyword argument -- positioning argument without minding order of parameter (must know the actual argument names)
# *args 
# **kwargs


# RETURN -- only returns without showing, u can later decide to print it or not. This ends a function and send a result back to the caller.
def square(number):
    # print(number * number) 
    # return None -- by default
    return (number * number) 
print(square(3))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
print(create_name("Dice", "Matt"))



# ======================> POSITIONAL ARGUMENTS <==============================
def greet_user(first_name, last_name, age):
    print(f"Hi {first_name} {last_name}!")
    # print("Welcome aboard")
    print(f"I am {age} years old")
    # Note: always give 3 line breaks after defining a function

print("Start")
greet_user(last_name='Amevye', first_name='Matthew', age=30)
# item_cost(total=50, shipping=5, discount=10)
print("Finish")

# CREATING REUSABLE FUNCTIONS
# 1st
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😠"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
        return output 
    
message = input(">")
print(emoji_converter(message))

# 2nd
def find_min(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number

# 3rd
# def allowed_dating_age(my_age):
#     girl_age = my_age / 2 + 7
#     return girl_age

# age = 35
# limit = allowed_dating_age(age)
# print("You are", age, "years old and you can date a ", round(limit), "years old girl or older")







# ======================> DEFAULT ARGUMENTS <==============================
# Defaukt value for certain parameters. Default is used when that argument is omitted. Makes your functions more flexible, reduces # of arguments

# def sentence(name='Matthew', action='Plays', item='football'):
#     print(name, action, item)

# sentence("Dan", "dance", "baloron")
# sentence(item='golf', action='plays', name='John')

# 2nd
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1- discount) * (1 +  tax)

print(net_price(500))
print(net_price(500, 0.1, 0))


# 3rd
import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep()
    print("DONE!")

count(0, 10)






# ======================> KEYWORD ARGUMENTS <==============================
# Preceded by an identifier, helps with readability. Order or arguments doesn't matter. You must know the exact paremeter name.
print(names, end=" ") # -- found within the print built-in function as a keyword argument. Mostly used in a loop to arrange horizontally.
print("1", "2", "3", "4", "5", sep="-")

# def gender(sex = "Unknown"):
#     if sex is "m":
#         sex = "male"
#     elif sex is "f":
#         sex = "female"
#     print(sex)
    
# gender("m")
# gender("f")
# gender()


# 1st
# Variable scope
# a = 1234
# def man():
#     print (a)

# def boy():
#     print(a)

# man()
# a = 9082
# boy()


# 2nd
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", "Spongebob", "Squarepants")


# 3rd
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=0, area=234, first=9064, last=3189)
print(phone_num)




# ======================> ARBITRARY  <==============================
# *args -- Allows u to pass multiple (non-key) arguments. (Tuples)
# **kwargs -- Allows u to pass multiple keyword arguments. {Dictionary}
# => unpacking operator
print(type(args))
print(type(kwargs))

# *args -- Allows u to pass multiple non-key arguments. (Tuples) --- Flexible number of aruments/loops/lists
# TUPLES ---Note: you must loop here/It must be an 
# 1st
def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(4)
add_numbers(4, 3, 3, 3)



# 2nd
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Dice", "Matt", "Lancelort")


# 3rd
def health_cal(age, apple_rate, cig_rate):
    age = (100 - age) + (apple_rate * 3.5) - (cig_rate * 2)
    print(age)

matt_data = [21, 30, 0]
# 1st
health_cal(matt_data[0], matt_data[1], matt_data[2])
# 2nd --Unpacking arguments
health_cal(*matt_data)
# 3rd--topols
x, y, z = (21, 30, 0)
health_cal(x, y, z)



# **kwargs -- Allows u to pass multiple keyword arguments. {Dictionary}
def print_address(**kwargs):

    # min_shares = min(zip(shares.values(), shares.keys())) -- dictionaries.py line 68.
    # for key, value in kwargs.keys():
    # for key, value in kwargs.value():
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="Mount Zion", 
              apt="100",
              city="Lafia", 
              state="Nasarawa", 
              zip="12345")