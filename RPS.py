import sys
import random

yn = "y"

print('Welcome to Rock Paper Scissors!')
while (yn != "n"):
    choice = input("Enter R(rock), P(paper), or S(scissors): ")
    print("Rock!")
    print("Paper!")
    print("Scissors!")
    print("Shoot!")
    randnum = random.randint(1, 3)
    if choice == "R":
        choiceS = "Rock"
        if randnum == 1:
            result = "Tie"
            compChoice = "Rock"
        if randnum == 2:
            result = "Loss"
            compChoice = "Paper"
        if randnum == 3:
            result = "Win"
            compChoice = "Scissors"
    if choice == "P":
        choiceS = "Paper"
        if randnum == 1:
            result = "Win"
            compChoice = "Rock"
        if randnum == 2:
            result = "Tie"
            compChoice = "Paper"
        if randnum == 3:
            result = "Loss"
            compChoice = "Scissors"
    if choice == "S":
        choiceS = "Scissors"
        if randnum == 1:
            result = "Loss"
            compChoice = "Rock"
        if randnum == 2:
            result = "Win"
            compChoice = "Paper"
        if randnum == 3:
            result = "Tie"
            compChoice = "Scissors"
    print("You chose " + choiceS + " and the computer chose " + compChoice)
    print("The result is a " + result + "!")
    yn = input("Would you like to play again? (y or n): ")
    

