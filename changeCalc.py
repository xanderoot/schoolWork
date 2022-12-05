import math
import random

input = random.randint(0,1000)
Dollars = 0
Quarters = 0
Dimes = 0
Nickels = 0
Pennies = 0
tempMath = 0

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