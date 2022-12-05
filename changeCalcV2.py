import math
import random

Dollars = 0
Quarters = 0
Dimes = 0
Nickels = 0
Pennies = 0
tempMath = 0

print('How much are you paying?')
changeGiven = float(input())
print('What is the bill?')
bill = float(input())
input2 = changeGiven - bill

changeGiven = int(changeGiven * 100)
bill = int(bill * 100)

input = changeGiven - bill

tempMath = (input / 100)
Dollars = math.floor(tempMath)
tempModulo = 0
tempModulo = input % 100
input = tempModulo

tempMath = (input / 25)
Quarters = math.floor(tempMath)
tempModulo = 0
tempModulo = input % 25
input = tempModulo

tempMath = (input / 10)
Dimes = math.floor(tempMath)
tempModulo = 0
tempModulo = input % 10
input = tempModulo

tempMath = (input / 5)
Nickels = math.floor(tempMath)
tempModulo = 0
tempModulo = input % 5
input = tempModulo

Pennies = input

noChange = 0

print()
print()

print('Total change is:', '%.2f' % input2)
print('You should leave the change as a tip!')

leftOverPercentage =  ((changeGiven - bill) / bill) * 100
print('If you do, that would be a', '%.2f' % leftOverPercentage + '% tip.')


if (leftOverPercentage < 19.5):  
    print('Thats not a very good tip.')
    if (leftOverPercentage < 5):
        print('You should be tipping way more.')
    tempBill = bill / 100
    twentyPercentTip = tempBill * 1.20
    newTip = twentyPercentTip - (bill / 100)
    amountToAdd = abs(input2 - newTip)
    print('You want to add',  '%.2f' % amountToAdd, 'to your total to tip at least 20%.')
elif ((leftOverPercentage > 40) and (leftOverPercentage < 99)):
    print('You just made your servers day by tipping that much.')
elif (leftOverPercentage > 100):
    print('Look at you! You truly appreciate the work your server put in.')
else:
    print('Thats a fantastic tip.')

print()

"""
if (Dollars != 0):
    if (Dollars == 1):
        print(Dollars, 'Dollar')
    else:
        print(Dollars, 'Dollars')
    noChange = 1
if (Quarters != 0):
    if (Quarters == 1):
        print(Quarters, 'Quarter')
    else:
        print(Quarters, 'Quarters')
    noChange = 1
if (Dimes != 0):
    if (Dimes == 1):
        print(Dimes, 'Dime')
    else:
        print(Dimes, 'Dimes')
    noChange = 1
if (Nickels != 0):
    if (Nickels == 1):
        print(Nickels, 'Nickel')
    else:
        print(Nickels, 'Nickels')
    noChange = 1
if (Pennies != 0):
    if (Pennies == 1):
        print(Pennies, 'Penny')
    else:
        print(Pennies, 'Pennies')
    noChange = 1
if (noChange == 0):
    print('No change')
"""