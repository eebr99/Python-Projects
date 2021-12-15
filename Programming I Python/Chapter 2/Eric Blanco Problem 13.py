#ask the length of the row (in feet) to assign to variable R
R = float(input('Enter the length of the row (in feet): '))

#ask for the amount of space used by an end-post assembly (in feet)
#to assign to variable E
E = float(input('Enter the amount of space used by an end-post assembly (in feet): '))

#ask the amount of space in between the lines (in feet) to assign to variable S
S = int(input('Enter the amount of space between the vines (in feet): '))

#assign the calculation to variable V
V = (R - (2*E)) // S

#display the number of grapevines that will fit in the row
print('The number of grapevines you can plant is:', V)
          

