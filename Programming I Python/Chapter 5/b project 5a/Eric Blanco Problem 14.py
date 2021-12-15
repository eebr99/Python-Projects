#Write a function name kinetic_energy that accepts an object's mass (in kg) and
#velocity (in m/s) as arguments. The function should return the amount of kinetic
#energy that object has. Write a program that asks the user to enter values for
#mass and velocity, the calls kinetic_energy to get the object's kinetic energy.

def main():
    print('This program calculates and displays kinetic energy of an object')
    print('with the values entered.')
    print()
    mass = float(input('Enter mass: '))
    velocity = float(input('Enter velocity: '))
    energy = kinetic_energy(mass, velocity)
    print('The kinetic energy is', format(energy, ',.2f'))


    
def kinetic_energy(m,v):
    KE = 0.5*m*v**2   #the book says the formula is 12mv2, but i think it means
    return KE         #the correct formula, which is (1/2)mv^2

main()
