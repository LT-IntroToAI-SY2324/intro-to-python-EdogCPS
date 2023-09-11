# We will write a rock paper scissors game in class - Complete it in this file
import random

print("\n\n")
#--------------------------------------------

def setDifficulty() -> int:
    difficulty = input('Enter a level. Your options are: \n1 : Impossibly Easy \n2 : Easy \n3 : Medium \n4 : Stalemate \n5 : Hard \n6 : Impossibly Hard\n').lower()
    try:
        difficulty = int(difficulty)
        # print(difficulty)
        # print(type(difficulty))
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

# retruns randComputerChoice(). just making my thinking easier to udnerstand. 
def medium() -> str:
    return randComputerChoice()

# returns player choice
def stalemate(p) -> str:
    return p

# 50% chance retruns rand choice, 50% time retruns the promt that mkes the computer win
def hard(p) -> str:
    if (randBool()):
        return impossiblyHard(p)
    return randComputerChoice()

# Returns the value that makes the computer win
def impossiblyHard(p) -> str:
    if (p == "rock"):
        return "paper"
    elif (p == "paper"):
        return "scissors"
    return "rock"

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
    print("You chose: " + p)
    print("Computer chose: " + c)
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
    elif (diff == 2):
        computer_choice = easy(player_choice)
    elif (diff == 3):
        computer_choice = medium()
    elif (diff == 4):
        computer_choice = stalemate(player_choice)
    elif (diff == 5):
        computer_choice = hard(player_choice)
    elif (diff == 6):
        computer_choice = impossiblyHard(player_choice)
    choices = {"player": player_choice, "computer": computer_choice}
    # print(choices)
    whoWon(choices)

# Asks for a difficulty, starts the game and re-runs it until hte play exits or goes to difficulty menu
def menu():
    while (True):
        diff = setDifficulty()
        if (diff == None):
            break # Player chose to quit
        continuePlaying = True
        while (continuePlaying):
            beginRound(diff)
            play_again = input('\nType anything to play again. \nType back to set difficulty. \nType quit to quit the game.\n').lower()
            if (play_again == "back"):
                print("\n")
                break
            elif (play_again == "quit"):
                continuePlaying = False

# the line of code that starts the whole program
menu()

#--------------------------------------------
print("\n\n")