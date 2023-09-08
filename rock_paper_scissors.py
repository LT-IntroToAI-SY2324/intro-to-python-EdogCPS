# We will write a rock paper scissors game in class - Complete it in this file
import random

print("\n\n")
#--------------------------------------------

def setDifficulty():
    difficulty = input('Enter a level. Your options are: \n1 : Impossibly Easy \n2 : Easy \n3 : Medium \n4 : Stalemate \n5 : Hard \n6 : Impossibly Hard\n').lower()
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
        elif (difficulty == "quit"):
            return None
    if (type(difficulty) == int):
        return difficulty

def randBool():
    return random.choice([True, False])
        
# retruns a random computer choice
def randComputerChoice():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    return computer_choice

# Returns the option that makes the player win
def impossiblyEasy(p) -> str:
    if (p == "rock"):
        return "scissors"
    elif (p == "paper"):
        return "rock"
    return "paper"

# 50% of the time it Returns the option that makes the play win, 50% it retruns a random answer
def easy(p) -> str:
    if (randBool()):
        return impossiblyEasy(p)
    return randComputerChoice()

# returns the user choice
def playerChoice():
    while (True):
        player_choice = input('Please enter a choice: rock, paper, or Scissors. \n').lower()
        if (player_choice == "rock" or player_choice == "paper" or player_choice == "scissors"):
            return player_choice
        elif (player_choice == "quit"):
            return None
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
def beginRound(diff):
    player_choice = playerChoice()
    if (diff == 1):
        computer_choice = impossiblyEasy(player_choice)
    elif (diff ==2):
        computer_choice = easy(player_choice)
    else:
        computer_choice = randComputerChoice()
    choices = {"player": player_choice, "computer": computer_choice}
    print(choices)
    whoWon(choices)

# Asks for a difficulty, starts the game and re-runs it until hte play exits or goes to difficulty menu
def menu():
    diff = setDifficulty()
    if (not diff == None):
        while (True):
            beginRound(diff)
            play_again = input('\nType anything to play again. \nType back to set difficulty. \nType quit to quit the game.\n').lower()
            if (play_again == "back"):
                print("\n")
                menu()
            elif (play_again == "quit"):
                break

menu()
#--------------------------------------------
print("\n\n")