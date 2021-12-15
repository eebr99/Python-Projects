#Write a function named "falling_distance" that accepts an object's falling time
#(in seconds) as an argument. The function should return the distance, in meters
#, that the object has fallen during the time interval.Write a program that
#calls the function in a loop that passes the values 1 through 10 as arguments
#and displays the return value.

def main():
    print("This program shows an object's fall distance (in meters) with each")
    print('passing second from 1 to 10.')
    print()
    print('Time(s)\tDistance(m)')
    print('--------------------')
    for time in range (10 + 1):
        distance = falling_distance(time)
        print(time, '\t', format(distance, ',.1f'))


def falling_distance(time):
    g = 9.8
    distance = 0.5*g*time**2 #I believe the formula is incorrect, i think it 
    return distance          #means (1/2)gt^2

main()
    
