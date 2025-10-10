# DUNDER -- Double underscore
# If __name__ == __main__: This script can be imported OR run standalone
# Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is modular,
                # helps reuseability,
                #  leaves no global variable,
                # avoid unintended execution)

                # Ex: library = import library for functionality when running library diectly. display a help page

def fav_food(food):
    print(f"Your favorite food is {food}")

def main():
    print(("This is script1"))
    fav_food("pizza")
    print("Goodbye!")

if __name__ == '__main__':
    main()