# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:41:52 2022

@author: jldju
"""
import random #For use of random() method choice(), it randomly selects an item from a list
import math #For use of math() method ceil(), it rounds a float up to the nearest interger

#function for user to choose number of rounds in the game
def numRounds():    
    goodInput = 'false' #Used to check proper user input
    while goodInput == 'false':
        rounds = int(input('Please enter number of rounds (1, 3, 5): '))
        if (rounds == 1) or (rounds == 3) or (rounds == 5):
            return(rounds)
        else:
            print('Please enter one of the choices listed!')

#function for user to pick 'rock', 'paper' or 'scissors'
def userPick(): 
    goodInput = 'false' #Used to check proper user input
    while goodInput == 'false':
        userSelection = input('Please enter "rock", "paper" or "scissors": ')
        userSelection = userSelection.lower() #sets input to lowercase to check for proper inputs
        if (userSelection == 'rock') or (userSelection == "paper") or (userSelection == "scissors"):
            return(userSelection)
        else:
            print('Please enter one of the choices listed!')
            
#function for game to pick 'rock', 'paper' or 'scissors'
def gamePick():
    gameList = ['rock', 'paper', 'scissors'] #List of Rock, Paper, Scissors options
    randomPick = random.choice(gameList)    #game's random selection from list
    return(randomPick)

#function to determine who won the round
def gameRound(userOption, gameOption):
    print('User picked {}, game picked {}.'.format(userOption, gameOption))
    if (userOption == 'rock') and (gameOption == 'paper'):
        return('gameWon')
    elif (userOption == 'rock') and (gameOption == 'scissors'):
        return('userWon')
    elif (userOption == 'paper') and (gameOption == 'rock'):
        return('userWon')
    elif (userOption == 'paper') and (gameOption == 'scissors'):
        return('gameWon')
    elif (userOption == 'scissors') and (gameOption == 'paper'):
        return('userWon')
    elif (userOption == 'scissors') and (gameOption == 'rock'):
        return('gameWon')
    else:
        return('draw')
        
    
def main():
    print('Welcome to this game of Rock Paper Scissors!')
    gameResults = [] #Track wins
    numGoes = numRounds()
    winsNeeded = math.ceil(numGoes/2)   #number of rounds needed to win match
    userWins = 0    #track user's rounds won
    gameWins = 0    #tracks game's rounds won
    
    #loop runs as long as we don't play user specified number of rounds
    #and neither the use or game have won enough rounds
    while (numGoes > 0) and (userWins != winsNeeded) and (gameWins != winsNeeded):
        userChoice = userPick()
        gameChoice = gamePick()
        roundResult = gameRound(userChoice, gameChoice)
        gameResults.append(roundResult) #Enters results into win tracker list
        #Output round result
        if roundResult == 'userWon':
            print('User wins the round!')
        elif roundResult == 'gameWon':
            print('Game wins the round!')
        else:
            print('Its a draw!')
        
        #increment loop variables
        numGoes -= 1
        userWins = gameResults.count('userWon') 
        gameWins = gameResults.count('gameWon') 
        
    #Output match results
    if userWins > gameWins:
        print('Congratulations, YOU WIN!!')
    elif gameWins > userWins:
        print('Sorry, YOU LOSE!!')
    else:
        print('The match is a DRAW!!')
        
    #Check if player wants to continue playing
    #and recursively calls main function if they do
    playStatus = input('Do you wish to play again? (yes or no) ')
    if playStatus.lower() == 'yes':
        main()
    else:
        print('Thank you for playing!')

if __name__ == '__main__':
    main()
