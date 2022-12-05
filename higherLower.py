#i got bored

import random

lowerBound = random.randint(0,45)
higherBound = random.randint(45,100)
randomNumber = random.randint(lowerBound,higherBound)

guessing = True
numOfGuesses = 0
while guessing == True:    
    game = True
    print('The number is between {} and {}.'.format(lowerBound,higherBound))
    while game == True:
        playerGuess = int(input('Enter your guess.'))        
        if playerGuess == randomNumber:
            print('Congrats! You guessed {} which is the number! It took you {} guesses.'.format(playerGuess,numOfGuesses))
            numOfGuesses = 0
            game = False
        elif playerGuess > randomNumber:
            print('Your guess is too high. Try again.')
            numOfGuesses += 1
        elif playerGuess < randomNumber:
            print('Your guess is too low.')
            numOfGuesses += 1
    if input('Try again?') == 'no':
        guessing = False
    