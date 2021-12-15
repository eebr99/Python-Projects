#write a function named 'max' that accepts two intger values as arguments and returns the value
#that is the greater of the two.

def main():
    print('This program takes two numbers and displays the greater of the two.')
    num1 = int(input('Enter the first number: '))    
    num2 = int(input('Enter the second number: '))
    greatest = max(num1, num2)
    print('The greater number is ', greatest)
    
def max(a, b):
    if a > b:
        greatest = a
    else:
        greatest = b
    return greatest

main()
