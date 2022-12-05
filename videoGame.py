import random
import urllib.request # this was also pulled from that section below
import math

# pulled from https://stackoverflow.com/questions/18834636/random-word-generator-python
# the url in the code i copied was borked. I found a different one and copied it in. it miraculously worked.
# is it plagarism if its programming? I don't care, this is programming, not philosophy
word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()

# nd copied programming

# variable declaration
numRooms = 14
totalRooms = 16
rooms = []
items = []
itemsCollected = 0
playerCoord = [0,0]
itemCoord = [0,0]
totalMoves = 0
# disclaimer about the next two lines. Im pretty sure its going to create some messed up items. I apologize in advance. Example, 'Staff of rape' is one I came across.
# honorable mentions while testing item creation. 'Stick of sometimes' 'Bottle of whale' 'String of consulting' 'Stick of construction' 'Wand of agreement'
# 'Hammer of unsubscribe' <- thats me after making a new account on a website and they send me marketing emails
words = long_txt.splitlines()
itemType = ['Gun','Sword','Wand','Staff','Hammer','Cudgel','Stick','Rock','Great Axe','Fist','String','Chopsticks','Whip','Bottle','List','Friend','Enemy','Book',]
roomType = ['Hall','Chamber','Dome','Observatory','Alcove','Cave','Kitchen','Bedroom','Bathroom']
forbiddenRooms = [[0,0,''],[3,3,'']]
# end of variable declaration

# room generation
# sixteen rooms will be created. 10 will contain items. 4 empty. one hard coded entrance and exit. upper left and lower right most likely.
# each room gets a coordinate, name, and status.
roomData = []
roomsCoords = [] #this should match 1 to 1 to the room data. its just the coords

for i in range(numRooms):
    roomDone = False
    tempWord = words[random.randint(0,len(words))]
    tempWord = tempWord.capitalize()
    tempRoomType = roomType[random.randint(0,len(roomType)-1)]
    tempNamedRoom = '{} of the {}'.format(tempRoomType,tempWord)
    while roomDone != True:
        roomXcoord = random.randint(0,3)
        roomYcoord = random.randint(0,3)
        tempCoord = [roomXcoord,roomYcoord]
        if tempCoord == [0,0] or tempCoord == [3,3]:
            continue
        elif tempCoord in roomsCoords:
            continue
        else:
            roomData.append([roomXcoord,roomYcoord,tempNamedRoom])
            roomsCoords.append(tempCoord)
            roomDone = True
roomData.insert(0, [0,0,'Entrance'])
roomsCoords.append([0,0])
roomData.append([3,3,'Boss Room'])
roomsCoords.append([3,3])
# end room generation

# item creation
for i in range(10):
    tempWord = words[random.randint(0,len(words))]
    tempWord = tempWord.capitalize()
    tempItemType = itemType[random.randint(0,len(itemType)-1)]
    tempNamedItem = '{} of {}'.format(tempItemType,tempWord)
    items.append(tempNamedItem)
# end item creation

# definition to save time when printing the visual. had to look up definitions. i figured python had them. I used them EXTENSIVELY in my java projects
def printDungeon(): 
    for i in range(4): #I dont like hard coding this but itll have to do. I dont know of a better way to make 16 rooms visually in text only
        xCoord = i
        for j in range(4):
            yCoord = j
            tempCoord = [i,j]
            if tempCoord == playerCoord:
                print('*',end=' ')            
            elif roomsCoords.count(tempCoord) == 0:
                print('O',end=' ')         
            else:
                temp = roomsCoords.index(tempCoord)
                print('X',end=' ')                
        print()
        xCoord += 1
# end definition

# move player definition
def playerMove(x):
    global totalMoves
    totalMoves += 1
    direction = x
    if direction == 'left':
        if playerCoord[1] - 1 < 0:
            print('Clean your glasses and try again. That is a wall.')
        else:
            playerCoord[1] -= 1
    elif direction == 'right':
        if playerCoord[1] + 1 > 3:
            print('Clean your glasses and try again. That is a wall.')
        else:
            playerCoord[1] += 1
    elif direction == 'up':
        if playerCoord[0] - 1 < 0:
            print('Clean your glasses and try again. That is a wall.')
        else:
            playerCoord[0] -= 1
    elif direction == 'down':
        if playerCoord[0] + 1 > 3:
            print('Clean your glasses and try again. That is a wall.')
        else:
            playerCoord[0] += 1
    else:
        print('That is not a direction.')
# end move player definition

# divine definition

def divine(): #copied from google. getting into philosophy again, is it possible to plagiarize math equations
    p1 = playerCoord
    p2 = itemCoord
    distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
    tempWord = words[random.randint(0,len(words))]
    tempWord = tempWord.capitalize()
    if p1 == p2:
        print('While you were getting ready to call upon another god, you trip on the item.')
    else:
        print('You call upon the power of a god to help you. {} responds and tells you it is {} rooms away.'.format(tempWord,math.floor(distance)))

# end divine definition

# item drop def

def itemDrop():
    itemDropped = False
    global itemCoord #thank you stack overflow for showing me 'global' though im not sure why i had to use it. playermove() properly updated the global variable
    while itemDropped == False:
        roomXcoord = random.randint(0,3)
        roomYcoord = random.randint(0,3)
        tempCoord = [roomXcoord,roomYcoord]
        if tempCoord == [0,0] or tempCoord == [3,3]:
            continue
        else:
            roomIndex = roomsCoords.index(tempCoord)
            if itemsCollected == 10:
                print('There are no more items. Procede to the final room.')    
            else:
                roomData[roomIndex][2] = items[itemsCollected]
                print('You hear an item pop into existence.')
            itemDropped = True
            itemCoord = tempCoord
# end item drop def

# main loop

playing = True
print('You wake up in a damp room.')
input('...')
itemDrop()
print('Before you can ponder what that sound was, a voice in your head begins talking.')
input('...')
print('I dont have long. There is a god slayer in this dungeon. Collect 10 items and bring them to the god killers chamber. He is in the far corner from you. Good luck.')
input('...')
printDungeon()
while playing == True:
    if playerCoord == [3,3] and itemsCollected < 10:
        print('It is too soon to fight the god killer. Leave immediately before he sees you!')
        playerCoord[0] -= 1
        printDungeon()
    elif playerCoord == [3,3] and itemsCollected >= 10:
        print('With one final look at the items youve collected, you enter the god killers chambers.')
        input('...')
        print('The lithe figure in front of you looks you over, eyes scanning over your entire body. "This is the child the gods have sent to fight me? Pathetic."')
        input('...')
        print('You feel your backpack start to shake. As you remove it, the shaking causes you to drop it items scattering everywhere.')
        input('...')
        print('Chuckling the god killer raises his hand and a ball of energy begins to form. "You arent a god, this wont hurt. I promise."')
        input('...')
        print('The items, still vibrating, begin to fly into the air. Different gods begin to materialize all forming a circle around the god killer.')
        input('...')
        print('"Enough! Your slaughter of the gods ends here." One of the gods charges forwards and strikes the god killer before the magical blast vaporizes them, weapon crashing to the ground.')
        input('...')
        print('One by one the gods all rush the god killer, each getting in a few hits before being vaporized. For every dead god, a new one materializes and picks up the previous weapon.')
        input('...')
        print('"No! I will not let you all ruin my lifes work."')
        input('...')
        print('For what felt like hours, the gods dueled with the increasingly gaunt man in front of you. Each hit seemed to do no damage but aged the man drastically.')
        input('...')
        print('You finally realize that the gods arent coming from nowhere. Each hit is freeing a god from the god killers body!')
        input('...')
        print('The gods also realizing this begin attacking with more vigor eventually defeating the husk of a man. As the body dissolves into dust, the gods fall silent.')
        input('...')
        print('"Thank you human. We can not thank you enough. Our fallen comrades did not die in vain. We will send you back to your realm now.')
        input('Press enter to return.')
        print('You moved {} times.'.format(totalMoves))
        playing = False
    else:
        print('What would you like to do? Move (up, down, left right), check, divine, loot, backpack.')
        desire = input()
        actions = desire.split()
        if actions == []: actions = 'easter egg'
        if actions[0] == 'move':
            playerMove(actions[1])
        elif actions[0] == 'check':
            if playerCoord == [0,0]:
                print('You are at the entrance of the dungeon.')
            elif playerCoord == [3,3]:
                print('You are at the boss room.')
            else:
                roomIndex = roomsCoords.index(playerCoord)
                print(roomIndex)
                print('You are in the',roomData[roomIndex - 1][2])
        elif actions[0] == 'divine':
            divine()
        elif actions[0] == 'loot':
            if itemCoord != playerCoord:
                print('There is nothing there.')
            else:
                print('A voice in your head tells you that is the {}.'.format(items[itemsCollected]))
                itemCoord = []
                itemsCollected += 1
                print('As you touch the item, it dematerilizes and your backpack feels slightly heavier. Almost in the same instant, you hear a pop somewhere nearby.')
                itemDrop()
        elif actions[0] == 'backpack': #im getting tired. its 12:12am. theres going to be a hanging comma. Im sorry.
            print('You have collected {} items.'.format(itemsCollected))
            for i in range(itemsCollected):
                print(items[i], end = ', ')
            print()
        elif actions[0] == 'debug':
            itemsCollected += 10
        elif actions == []:
            print('Sorry I couldnt understand you. Can you try that again?')
        else:
            print('Sorry I couldnt understand you. Can you try that again?')
        printDungeon()
# end main loop

