# CITC-2391-C01 Summer 2020
# Program 1
# Name: Kylan McLin
# Date: 7/19/2020
# Lab3

import random


# function for title message
def title_message():
    print("Dice Roller")
    print()


# set up roll function for rolling one die
def roll():
    value = random.randint(1, 6)
    return value


# set up roll_dice function
def roll_dice():
    die1 = roll()
    die2 = roll()

    total = die1 + die2

    print("Die 1: ", die1)
    print("Die 2: ", die2)
    print("Total: ", total)

    if die1 == 1 and die2 == 1:
        print("Snake eyes!")
    elif die1 == 6 and die2 == 6:
        print("Boxcars!")
    print()


# set up main function
def main():
    title_message()

    choice = input("Roll the dice? (y/n): ")

    while choice.lower() != "n":
        roll_dice()
        choice = input("Roll again? (y/n): ")
    print("Bye!")


# call main function
if __name__ == '__main__':
    main()
