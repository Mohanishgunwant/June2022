
"""The goal is to create a program that will simulate the roll of dice."""
"""Adding 2 rules
1: Player will get another chance if 6 comes
2: Player will not get another chance as well as the gain will be lost if the player gets 6 consecutive 6s"""

import random
number = random.randint(1,6)
number1 = random.randint(1,6)
number2 = random.randint(1,6)
r = input("roll the dice by pressing letter r: ")
print("you have got",number)
if number == 6:
    print("you are lucky you have another chance so press r")
    r = input("roll the dice by pressing letter r: ")
    print("you have got", number1)
if number1 == 6 and number==6:
    print("you are lucky you have another chance so press r")
    r = input("roll the dice by pressing letter r: ")
    print("you have got", number2)
if number2==6 and number1==6 and number==6:
    print("Sorry, consecutive three 6, you have lost your gain")