# WHILE LOOPS
guess_count = 1
while guess_count <= 5:
    print('*' * guess_count)
    guess_count = guess_count + 1
print("Done") 

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Gues: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry you failed!')

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started: 
            print("Car is already started!...")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!..")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the car
    """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand the ")


# FOR LOOPS
