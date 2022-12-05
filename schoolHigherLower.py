#i got bored
import random

guessing = True
numOfGuesses = 0
while guessing == True:    
    game = True
    lowerBound = int(input('What is the lowest number? '))
    higherBound = int(input('What is the Highest number? '))
    randomNumber = random.randint(lowerBound,higherBound)
    print('The number is between {} and {}.'.format(lowerBound,higherBound))
    while game == True:
        playerGuess = int(input('Enter your guess. '))        
        if playerGuess == randomNumber:
            print('Congrats! You guessed {} which is the number! It took you {} guesses.'.format(playerGuess,numOfGuesses)) #pretend i did an if statement to change the print for guess or guesses
            numOfGuesses = 0
            game = False
        elif playerGuess > randomNumber:
            print('Your guess is too high. Try again.')
            numOfGuesses += 1
        elif playerGuess < randomNumber:
            print('Your guess is too low. Try again.')
            numOfGuesses += 1
    if input('Try again? "yes" or "no". ') == 'no':
        guessing = False