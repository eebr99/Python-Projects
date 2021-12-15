#Write a program that predicts the approximate size of a population of
#organisms.
print('This program will predict the approximate size of a population')
print('using the data entered.')
print()

pop = int(input('Starting number of organisms: '))
growth = int(input('Average daily increase (as a percentage): '))
days = int(input('Number of days to multiply: '))
percent = growth / 100

print()
print('Day\tApproximate Population')
print('---------------------------')
print('1\t', pop)

for counter in range(2, days+1):
    pop = pop + (percent * pop)
    print(counter, '\t', pop)
