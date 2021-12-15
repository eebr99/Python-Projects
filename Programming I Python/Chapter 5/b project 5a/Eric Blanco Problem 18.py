#Write another program that displays all of the prime numbers from 1 to 100.
#the program should have a loop that calls the is_prime function.

def main():
    print('This program displays all prime numbers from 1 to 100.')
    print()
    print('Number')
    print('------')
    for num in range (1, 100 + 1):
        is_prime(num)
        if is_prime(num) == True:
            print(num)

def is_prime(a):
    value = int(a / 2)
    num = True
    for i in range (2, value + 1):
        if (a % i) == 0:
            num = False
    return num

main()
