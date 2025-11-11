from models import Pets, session
import os


def view_pets(current_user):
    for current_pet in current_user.pets:
        print("Pets R Us - View My Pets")
        print("Here is a list of your beloved pets!: ")
        print(
            f"Name: {current_pet.name}, Species: {current_pet.species}, Breed: {current_pet.breed}, Age: {current_pet.age}"
        )


def create_pet(current_user):
    os.system("cls" if os.name == "nt" else "clear")
    print("Pets R Us - Create Pet")
    print("A new pet! Hisssss! Bark! Chirp!")

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


def update_pet(current_user):
    os.system("cls" if os.name == "nt" else "clear")
    print("Pets R Us - Update Pet")
    print("Lets get fido updated!")

    print("Here is a list of your pets: ")
    print("Select the number of the pet you want to update:")
    while True:
        try:
            counter = 1
            for current_pet in current_user.pets:
                print(f"{counter} - Name: {current_pet.name}")
                counter += 1

            pet_choice = int(input("Enter number: ")) - 1

            if pet_choice < 0 or pet_choice >= len(current_user.pets):
                print("Thats not a valid pet number silly! Please try again.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    get_pet = current_user.pets[int(pet_choice)]

    for field in get_pet.__table__.columns.keys():
        if field in ["id", "owner_id"]:
            continue
        current_value = getattr(get_pet, field)
        new_value = input(f"Enter new {field} (current: {current_value}): ")
        if new_value:
            setattr(get_pet, field, new_value)

    print("Updating pet info...")
    session.commit()
    return


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
