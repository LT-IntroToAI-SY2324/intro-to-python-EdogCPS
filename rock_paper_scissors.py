# We will write a rock paper scissors game in class - Complete it in this file
import random

print("\n\n")
#--------------------------------------------

def setDifficulty():
    difficulty = input('Enter a level. Your options are: \n1 : Impossibly Easy \n2 : Easy \n3 : Medium \n4 : Stalemate \n5 : Hard \n6 : Impossibly Hard').lower()
    try:
        difficulty = int(difficulty)
    except:
        if (difficulty == "impossibly easy"):
            difficulty = 1
        elif (difficulty == "easy"):
            difficulty = 2
        elif (difficulty == "Medium"):
            difficulty = 3
        elif (difficulty == "stalemate"):
            difficulty = 4
        elif (difficulty == "hard"):
            difficulty = 5
        elif (difficulty == "impossibly hard"):
            difficulty = 6
    if (type(difficulty) == int):
        #return or somting


# retruns a random computer choice
def randComputerChoice():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    return computer_choice

# returns the user choice
def playerChoice():
    while (True):
        player_choice = input('Please enter a choice: rock, paper, or Scissors. \n').lower()
        if (player_choice == "rock" or player_choice == "paper" or player_choice == "scissors"):
            return player_choice
        print("Not a valid option.\n")

# prints out who won the round and with what
def whoWon(o):
    p = o["player"]
    c = o["computer"]
    print(p)
    print(c)
    if (p == c):
        print("TIE! Both players chose " + c)
    elif (p == "rock" and c == "paper"):
        print("Computer wins! paper beats Rock!")
    elif (p == "paper" and c == "scissors"):
        print("Computer wins! scissors beats paper!")
    elif (p == "scissors" and c == "rock"):
        print("Computer wins! rock beats scissors!")
    else:
        print("You win! " + p + " beats " + c + "!")

# Obtains calls respetcve functions to obtain both comuter and player choice and returns a dictoranry with their choices
def beginRound():
    player_choice = playerChoice()
    choices = {"player": player_choice, "computer": randComputerChoice()}
    print(choices)
    whoWon(choices)

beginRound()

#--------------------------------------------
print("\n\n")