from models import Pets, session


def view_pets(current_user):
    for current_pet in current_user.pets:
        print("Pets R Us - View My Pets")
        print("Here is a list of your beloved pets!: ")
        print(
            f"Name: {current_pet.name}, Species: {current_pet.species}, Breed: {current_pet.breed}, Age: {current_pet.age}"
        )


def create_pet(current_user):
    print("Pets R Us - Create Pet")
    new_pet = Pets(owner_id=current_user.id)
    pet_info = {"name": "", "species": "", "breed": "", "age": ""}

    for key in pet_info:
        pet_info[key] = input(f"Enter your pet's {key.title()}: ")

    try:
        if current_user:
            new_pet = Pets(owner_id=current_user.id, **pet_info)
            session.add(new_pet)
            session.commit()
            print("New pet created successfully!")
            print(
                f"Name: {new_pet.name}, Species: {new_pet.species}, Breed: {new_pet.breed}, Age: {new_pet.age}"
            )
    except Exception as e:
        print(f"An error occurred while creating the pet: {e}")
        print("Make sure Spike in not an the keyboard!")


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
