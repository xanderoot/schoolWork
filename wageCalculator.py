import random

hoursWorked = random.randint(1,80)
hourlyRate = random.randint(1,80)
overtimeThreshold = 40 #leaving this hardcoded for the sake of randomness simplicity'
overtimeRate = int(hourlyRate * 1.30) #30% more. arbitrary number. I could randomize that too but thats just silly
overtimeHours = hoursWorked % overtimeThreshold
taxRate = random.randint(1,10)# I really like random numbers as variables

print()

if (overtimeHours == hoursWorked):
    regularPay = hoursWorked * hourlyRate
    print('You worked {} hours at a rate of {} per hour for a total of {}.'.format(hoursWorked,hourlyRate,regularPay))
    taxableAmount = regularPay

else:
    regularPay = overtimeThreshold * hourlyRate
    overtimePay = overtimeHours * overtimeRate
    print('You worked', hoursWorked, 'hours at a rate of', hourlyRate)
    print('{} of your {} hours was at an overtime rate of {}.'.format(overtimeHours,hoursWorked,overtimeRate))
    total = regularPay + overtimePay
    print('You earned in total', total)
    taxableAmount = total

taxValue = taxRate / 100
tax = int(taxableAmount * taxValue)
paycheckAfterTax = taxableAmount - tax
taxRate = str(taxRate)
print('The local tax rate is {}% leaving you with {} remaining'.format(taxRate,paycheckAfterTax))
print()
