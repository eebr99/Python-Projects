#write a program thats asks user to enter number of packages purchased
#and the display the amount of the discount as wll as the total amount of the
#purchase after the discount

price = int(99)
packages = int(input('Enter the number of packages purchased today: '))
subtotal = (price * packages)

if packages < 10:
    print('No discount applied, your total is: $', price * packages, sep='')
elif packages >= 10 and packages <= 19:
    print('10% discount applied, your total is: $', subtotal - (subtotal * .10), sep='')
elif packages >= 20 and packages <= 49:
    print('20% discount applied, your total is: $', subtotal - (subtotal * .20), sep='')
elif packages >= 50 and packages <= 99:
    print('30% discount applied, your total is: $', subtotal - (subtotal * .30), sep='')
else:
    packages >= 100
    print('40% discount applied, your total is: $', subtotal - (subtotal * .40), sep='')
