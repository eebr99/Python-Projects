#Assign values to P, r, n, t; calculate A and display

#Get the amount of principal originally deposited into account and assign to P
P = float(input('Enter the amount of principal originally deposited into account: '))

#Get the annual interest rate and assign to r
r = float(input('Enter the annual interest rate: '))

#Get the number of times compounded per year and assign to n
n = float(input('Enter the number of times per year the interest is compounded: '))

#Get the number of years and assign to t
t = float(input('Enter the number of years the account will be left to earn interest: '))

#Assign to A by calculation
A = P * ((1 + r / n) ** (n * t))

#Display the amount of money in the account after specified number of years
print('The amount of money in the account after the specified number of years will be:$', A)
