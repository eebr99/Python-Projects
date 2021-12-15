
#write a program that asks the user to enter the weight of a package
#and then displays the shipping charges.

weight = float(input('Enter the weight of your package: '))
#assign a value to ship_charge as well

if weight <= 2.0:
    ship_charge = weight * 1.50
    print('You will be charged $', ship_charge, sep='')
else:
    if weight > 2 and weight <=6:
        ship_charge = weight * 3.00
        print('You will be charged $', ship_charge, sep='')
    else:
        if weight > 6 and weight <= 10:
            ship_charge = weight * 4.00
            print('You will be charged $', ship_charge, sep='')
        else:
            weight > 10
            ship_charge = weight * 4.75
            print('You will be charged $', ship_charge, sep='')
