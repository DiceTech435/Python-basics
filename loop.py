# LOOPS
# while
# for in
# do while

# # WHILE LOOPS
# # 1st
# guess_count = 1
# while guess_count <= 5:
#     print('*' * guess_count)
#     guess_count = guess_count + 1
# print("Done") 

# # 2nd
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Gues: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else:
#     print('Sorry you failed!')


# # 3rd
# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started: 
#             print("Car is already started!...")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!..")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit the car
#     """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand the ")


# # FOR LOOPS/FOREACH
# # 1st
# for item in 'python':
# for item in ["1, 2, 3, 4, 5"]:
# for item in range(10):
# for item in range(5, 10, 2):
    # print(item)

# # 2nd
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Toal: {total}")

# # NESTED LOOPS
# 1st
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# 2nd
# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     # print('x' * x_count)
#     output = ''
#     for count in range(x_count):
#         output += 'a'
#     print(output)
