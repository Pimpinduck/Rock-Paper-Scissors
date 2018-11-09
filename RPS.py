import sys
import random
import time

yn = "y"
gameCount = 1
playerWin = 0
compWin = 0

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
    time.sleep(1)
    randnum = random.randint(1, 3) #Choosing a random choice for the computer
    if choice == "R" or choice == "r": # If statements to determine what should be displayed to the user at the end
        choiceS = "Rock"
        if randnum == 1:
            result = "Tie"
            compChoice = "Rock"
        if randnum == 2:
            result = "Loss"
            compChoice = "Paper"
            compWin += 1
        if randnum == 3:
            result = "Win"
            compChoice = "Scissors"
            playerWin += 1
    if choice == "P" or choice == "p": #Added more user options
        choiceS = "Paper"
        if randnum == 1:
            result = "Win"
            compChoice = "Rock"
            playerWin += 1
        if randnum == 2:
            result = "Tie"
            compChoice = "Paper"
        if randnum == 3:
            result = "Loss"
            compChoice = "Scissors"
            compWin += 1
    if choice == "S" or choice == "s": #Added more user options
        choiceS = "Scissors"
        if randnum == 1:
            result = "Loss"
            compChoice = "Rock"
            compWin += 1
        if randnum == 2:
            result = "Win"
            compChoice = "Paper"
            playerWin += 1
        if randnum == 3:
            result = "Tie"
            compChoice = "Scissors"
    print("\nYou chose " + choiceS + " and the computer chose " + compChoice + "\n") #showing the result of the game to the user
    print("The result is a " + result + "!\n")  #Printing result absolutely
    print("The current standings are:")
    print("You: " + str(playerWin) + "/" + str(gameCount))
    print("Computer: " + str(compWin) + "/" + str(gameCount) + "\n")
    gameCount += 1
    yn = input("Would you like to play again? (y or n): ") #Play again Y or N
    

