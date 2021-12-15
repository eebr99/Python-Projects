#Write a program that lets the user enter a nonnegative integer then uses a loop
#to calculate the factorial of that number. Display the factorial.

total = 1
integer = int(input('Enter any non negative number you want to calculate the '\
                    'factorial of: '))

for number in range(1, integer + 1):
    total *= number

print('The factorial is: ', total)

