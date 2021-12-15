#Write a Boolean function name 'is_prime' which takes an integer as an argument and
#returns true if the argument is a prime number, or false otherwise.

def main():
    print('This program will take a number you enter and determine if it is prime.')
    integer = int(input('Enter a number: '))
    num = is_prime(integer)
    if num == True:
        print(integer, 'is prime.')
    else:
        print(integer, 'is not prime.')

def is_prime(a):
    value = int(a / 2)
    num = True
    for i in range (2, value + 1):
        if (a % i) == 0:
            num = False
    return num

main()
