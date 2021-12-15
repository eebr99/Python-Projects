#Write a program that displays a stair-step pattern with spaces in between
# the # character.

steps = 6

for r in range(steps):
    print('#', end='')
    for c in range(r):
        print(' ', end='')
    print('#')
