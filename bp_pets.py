from models import Pets, session


def view_pets(current_user):
    for current_pet in current_user.pets:
        print("Pets R Us - View My Pets")
        print("Here is a list of your beloved pets!: ")
        print(
            f"Name: {current_pet.name}, Species: {current_pet.species}, Breed: {current_pet.breed}, Age: {current_pet.age}"
        )


def create_pet(current_user):
    pass


# Create pets function
# gets pets info from user
# create Pets() from the info
# print new pet


# Update pets function
# display current users pets
# allow them to select a pet BY NAME
# query that pet from the database
# get updated info from the user
# set that pets info to the new info
# commit changes
# print new pet info


# Delete pets function
# display current users pets
# allow them to select a pet BY NAME
# query that pet from the database
# Ask user if they are sure they want to delete this pet
# delete pet from the session
# commit changes
