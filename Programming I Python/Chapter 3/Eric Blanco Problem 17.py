#Create a program that leads a person through the steps of fixing a bad
#wifi connection. Reference flowchart in book.

print('Reboot the computer and try to connect.')

answer = input('Did that fix the problem? ')

if answer == 'yes':
    print('')
else:
    print('Reboot the router and try to connect.')
    answer = input('Did that fix the problem? ')
    if answer == 'yes':
        print('')
    else:
        print('Make sure the cables between the router & modem are plugged in firmly.')
        answer = input('Did that fix the problem? ')
        if answer == 'yes':
            print('')
        else:
            print('Move the router to a new location and try to connect.')
            answer = input('Did that fix the problem? ')
            if answer == 'yes':
                print('')
            else:
                print('Get a new router.')

