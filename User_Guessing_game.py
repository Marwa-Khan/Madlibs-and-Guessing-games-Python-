#2nd Project
print("\n\n------------Write a program that will ask the user to guess the correct number----------------\n\n")

#library to create a random number
import random


#function definition
def guess_no(ending_no):
    random_num=random.randint(1,ending_no)
    guess_num=0
    while guess_num!=random_num:
        guess_num=int(input("Enter the guess between 1 and " +str(ending_no) +":"))
        if guess_num>random_num:
            print("\nYou have guessed the high number,Try again!\n")
        elif guess_num<random_num:
            print("\nYou have guessed the low number,Try again!\n")
        else:
            print("\nCongrats! You have guessed the correct number\n")


#function call
guess_no(30)



