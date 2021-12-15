import PetMod

def main():
    print("Hello!")
    print('Today we will be collecting some basic info about your pet.')
    print()

    name = input("What is your pet's name? ")
    animal_type = input("What type of animal is your pet? ")
    age = input("How old is your pet? ")

    pet = PetMod.Pet(name, animal_type, age)
    print()
    print("Here is the data you entered.")
    print()
    print('Name: ', pet.get_name())
    print('Animal Type: ', pet.get_animal_type())
    print('Age: ', pet.get_age())

main()
