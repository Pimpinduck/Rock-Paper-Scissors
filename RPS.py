import sys
import random
import time

yn = "y"

print('Welcome to Rock Paper Scissors!')
while (yn != "n" and yn != "N"): #Starting off the loop
    choice = input("Enter R(rock), P(paper), or S(scissors): ") #Gathering the user's choice
    print("Rock!") #Fun little intro
    time.sleep(1)
    print("Paper!")
    time.sleep(1)
    print("Scissors!")
    time.sleep(1)
    print("Shoot!")
    randnum = random.randint(1, 3) #Choosing a random choice for the computer
    if choice == "R" or choice == "r": # If statements to determine what should be displayed to the user at the end
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
    if choice == "P" or choice == "p": #Added more user options
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
    if choice == "S" or choice == "s": #Added more user options
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
    print("You chose " + choiceS + " and the computer chose " + compChoice) #showing the result of the game to the user
    print("The result is a " + result + "!")  #Printing result absolutely
    yn = input("Would you like to play again? (y or n): ") #Play again Y or N
    

