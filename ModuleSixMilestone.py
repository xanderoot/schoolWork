# Chase Chovanec

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }
'''
this is not modular and therefore very prone to errors as you expand the map if you are entering it manually.
though i understand the scope of this assignment.

it is 4:46 pm right now as im writing this line.
i am going to see how simple i can make this assignment.
all im doing is taking an input and if it matches a key in a dict entry setting player location to the key value. Thats stupid simple.
'''

playerLocation = 'Great Hall' # hardcoded values are bad!
possibleMoves = rooms[playerLocation]

while True:
    print('\n\n\n\n\n\nNorth, East, South, or West? Exit or ctrl + c to exit.\n')
    print('Your location is: {}\n'.format(playerLocation))
    print('Your possible moves are:')
    for move in possibleMoves: # prints list of possible moves
        print('    {} to the {}.'.format(move,possibleMoves.get(move)))
    playerIntention = input().capitalize() # player input
    if playerIntention in possibleMoves: # checks if move is in dict and moves if True
        playerLocation = possibleMoves.get(playerIntention)
        possibleMoves = rooms[playerLocation]
    elif playerIntention == 'Exit': # catches exit 
        print('Thank you for playing.')
        break
    else:
        print('')
'''
okay it is now 5:14 dead on 30 minutes to do that. I spent more time on prettifying the output than coding
im going to go through the rubric and check of things i needed to do

1 i watched the video
2 i named the file.
  i wrote my name in a comment
  its 14 lines of looping code that are fairly straightforward in nature
3 copied the provided dict
4 see above for the code. This is 100% fundamentally different from my project 1 code.
5 the way that I check the input means it will only accept moves in the dict. 
  invalid moves will be caught by the else statement.
  the player has multiple ways to exit the game

okay this is funny, the instant feedback tool had no feedback
https://i.imgur.com/xwRDWvI.png
https://i.imgur.com/4hMoDLT.png
https://i.imgur.com/nHU3xDV.png
https://i.imgur.com/OYbHjkl.png

'''
