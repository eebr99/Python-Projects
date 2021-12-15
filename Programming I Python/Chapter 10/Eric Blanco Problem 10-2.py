import CarMod

def main():
    my_car = CarMod.Car('2020', 'Ford')


    print('Hello! We will be taking your car for a test ride.')
    print()
    print('We will now speed up by 5.')
    print()
    
    for i in range(5):
        my_car.accelerate()
        print('The current speed of your car is ', my_car.get_speed())

    print()
    print('We will now begin braking.')
    print()

    for i in range(5):
        my_car.brake()
        print('The current speed of your car is ', my_car.get_speed())

    print()
    print('Your car is in working order. Have a nice day!')

main()
