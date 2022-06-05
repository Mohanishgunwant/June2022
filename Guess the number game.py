"""
The main goal of the project is to create a program that randomly select a number in a range
then the user has to guess the number. user has three chances to guess the number if he guess
correct then a message print saying “you guess right “otherwise a negative message prints.

"""

import random
for i in range(0,3):
    choosen_number = int(input("Choose a number between 0 to 20: "))
    number= random.randint(0,10)
    if choosen_number == number:
        print("You guess right")
    else:
        print("Unfortunately, you guessed it wrong")


