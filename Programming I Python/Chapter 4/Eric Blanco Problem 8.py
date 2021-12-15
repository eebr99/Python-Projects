#Write a program with a loop that asks the user to enter a series of positive
#numbers. The user should enter a negative number to signal the end of the
#series. After all the positive numbers have been entered, the program
#should display their sum.

print('This program calculates the sum of')
print('a series of positive numbers you enter.')
print('When you are finished entering numbers, enter a negative number to end.')

total = 0.0
number = 0.0

while number >= 0:
    total = total + number
    number = int(input('Enter a positive number: '))
print('The sum of the numbers entered is: ', total)
    
