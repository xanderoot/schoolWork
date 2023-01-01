import random
import time

rooms = {
    'Ballroom': {'East': 'Banquet', 'South': 'Library'},
    'Banquet': {'West': 'Ballroom', 'East': 'Kitchen', 'South': 'Study'},
    'Kitchen': {'West': 'Banquet', 'South': 'Pantry'},
    'Library': {'North': 'Ballroom', 'East': 'Study', 'South': 'Conservatory'},
    'Study': {'North': 'Banquet', 'West': 'Library', 'South': 'Attic'},
    'Pantry': {'North': 'Kitchen','South': 'Basement'},
    'Conservatory': {'North': 'Library', 'West': 'Garden'},
    'Attic': {'North': 'Study'},
    'Garden': {'East': 'Conservatory'},
    'Basement': {'South': 'Dungeon','North': 'Pantry'},
    'Dungeon': {'North': 'Basement'},
}
roomIndex = []
for key, value in rooms.items():
    roomIndex.append(key)

playerLocation = roomIndex[random.randint(0,len(roomIndex) - 1)]
possibleMoves = rooms[playerLocation]
itemLocations = []
numberOfItems = 10 #all rooms will have an 
if numberOfItems > len(roomIndex) - 1: 
    raise Exception('error: too many item requests for the number of rooms. either rewrite code or change numberOfItems value.')
playerItems = 0
tempRooms = roomIndex.copy()
tempRooms.pop(-1) #all rooms will have an 


for x in range(numberOfItems): # creates the list of rooms for the items to be in. also removes dungeon from list
    roomID = random.randint(0,len(tempRooms)-1)
    itemLocations.append(tempRooms[roomID])
    tempRooms.pop(roomID)

itemLocations.append(' ')
    
playerAttempts = 0
firstRun = True


while True: # main game loop
# opening statement disables after first loop   
    if firstRun == True:
        print('\n\n\n\n\n\n\n\n\n\nWhere oh where is that thing you just put down.')
        time.sleep(3)
        firstRun = False
# lose condition
    if playerAttempts >= 10:
        print('\n\n\n\n\n\n\n\n\nYou are too fatigued to continue searching and collapse drifting off to sleep.\n')
        playerLocation = 'Dungeon'
# win condition
    if playerLocation == 'Dungeon' and playerItems >= 10:
        print('\n\n\n\n\n\n\n\n\nOpening the door to the dungeon you have a moment of inspiration')
        print("You open the hatch you find the thing you've been looking for hours!\nTurns out the villain was your own forgetfulness.")
        print('Of course its in the last place you would expect.')
        print('You win!')
        break
# loss story
    if playerLocation == 'Dungeon' and playerAttempts >= 10:
        print('Walking into the dungeon you collapse onto the bed after searching for so long and finding nothing.')
        input()
        print('You drift off to sleep and begin to dream.')
        input()
        print('\n\n\n\n\n\n\n\n\nGrandpa Joe: Mr. Wonka?')
        input()
        print('\nWilly Wonka: I am extraordinarily busy, sir.')
        input()
        print('\nGrandpa Joe: I was just wondering about the chocolate - Uh, the lifetime supply of chocolate... for Charlie. When does he get it?')
        input()
        print("\nWilly Wonka: He doesn't.")
        input()
        print('\nGrandpa Joe: Why not?')
        input()
        print('\nWilly Wonka: Because he broke the rules.')
        input()
        print("\nGrandpa Joe: What rules? We didn't see any rules. Did we, Charlie?")
        input()
        print('\nWilly Wonka: Wrong, sir! Wrong! Under section 37B of the contract signed by him, it states quite clearly that all offers shall become null and void if - and you can read it for yourself in this photostatic copy - "I, the undersigned, shall forfeit all rights, privileges, and licenses herein and herein contained," et cetera, et cetera..."Fax mentis incendium gloria cultum," et cetera, et cetera..."Memo bis punitor delicatum!" It is all there, black and white, clear as crystal! You stole fizzy lifting drinks. You bumped into the ceiling which now has to be washed and sterilized, so you get nothing! You lose! Good day sir!')
        input()
        print("\nGrandpa Joe: You're a crook. You're a cheat and a swindler! How could you do a thing like this, raise up a little boy's hopes and then dash all his dreams to pieces? You're an inhuman monster!")
        input()
        print('\nWilly Wonka: I said "Good day!" ')
        input()
        print('Try again? (y/n)')
        if input() == 'y':
            continue
        else: break
# loss condition prevention
    if playerLocation == 'Dungeon' and playerAttempts >= 5:
        choice = input('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Take a nap? (y/n)')
        if choice == 'n':
            print('\n\n\n\n\n\n\n\n\nYou resume the arduous search. You exit the dungeon.')
            playerLocation = 'Basement'
        else:
            print('\n\n\n\n\n\n\n\n\nYou resolve to try again after this nap.\nYou feel renewed.\n(Attempts reduced by 5.)\n')
            playerAttempts -= 5
            input()
#  fatigue warning
    if playerAttempts >= 5: print('\n\n\n\n\n\n\n\n\nYou are feeling fatigued, feel free to retire to the dungeon for a nap to keep your energy up. Pushing yourself too hard is dangerous.')
# win condition display   
    if playerItems >= 10: print('\n\n\n\n\n\n\n\n\nGoal: Okay you have checked everywhere maybe you left it at your desk in the dungeon.\n')
# notification that you are in the room you want to search
    elif playerLocation == itemLocations[0]: print('\n\n\n\n\n\n\n\n\nGoal: Search for the item.\n')
# general status notification
    else: print('\nGoal: Search rooms until you find the item. {} left to search.\n\nYou think maybe you left it in the {}\n\nYour location is: {}\n'.format(10 - playerItems,itemLocations[0],playerLocation))

# possible moves and main screen display
    print('Your possible moves are North, East, South, or West, Search, or ctrl-c to close.\n')
# prints list of possible moves    
    for move in possibleMoves: 
        print('    {} to the {}.'.format(move,possibleMoves.get(move)))
# player input
    playerIntention = input().capitalize() 
# checks if move is in dict and moves if True
    if playerIntention in possibleMoves: 
        playerLocation = possibleMoves.get(playerIntention)
        possibleMoves = rooms[playerLocation]
# sets player location to room
    elif playerIntention in rooms: 
        playerLocation = playerIntention
        possibleMoves = rooms[playerLocation]
# if item is in room add to count and remove from list
    elif playerIntention == 'Search' and itemLocations[0] == playerLocation: 
        input('\n\n\n\n\n\n\n\n\n\n\n\n\nYou search and search and search. Tearing up the room turns up nothing.')
        playerItems += 1
        playerAttempts += 1
        itemLocations.pop(0)
# if room empty increment attempts
    elif playerIntention == 'Search' and itemLocations[0] != playerLocation: 
        playerAttempts += 1
        input('\n\n\n\n\n\n\n\n\n\n\n\n\nYou are pretty sure the item is not here.')
    elif playerIntention == 'Debugwin': playerItems += 10 # 'That was easy.' - Easy Button
    elif playerIntention == 'Debuglose': playerAttempts =+ 10 # 'YOU GET NOTHING. YOU LOSE. GOOD DAY SIR!' Mr Wonka
    else: print('Try Again') # player cant see this either.