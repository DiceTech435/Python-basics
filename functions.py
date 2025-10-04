# FUNCTIONS def -- reusable block of code
# Paramters -- placeholders for recieving informations on a defined function
# Arguments -- value supplied to a function
# Keyword argument -- positioning argument without minding order of parameter (must know the actual argument names)

def greet_user(first_name, last_name, age):
    print(f"Hi {first_name} {last_name}!")
    # print("Welcome aboard")
    print(f"I am {age} years old")


print("Start")
greet_user(last_name='Amevye', first_name='Matthew', age=30)
# item_cost(total=50, shipping=5, discount=10)
print("Finish")


# RETURN -- only returns without showing, u can later decide to print it or not
def square(number):
    # print(number * number) 
    # return None -- by default
    return (number * number) 
print(square(3))


# CREATING REUSABLE FUNCTIONS