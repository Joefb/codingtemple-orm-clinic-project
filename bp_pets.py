from models import Pets, session
import os


def view_pets(current_user):
    os.system("cls" if os.name == "nt" else "clear")
    print("Pets R Us - View My Pets")
    print("Here is a list of your beloved pets!: ")
    print("-----------------------------------")
    for current_pet in current_user.pets:
        print(
            f"Name: {current_pet.name}, Species: {current_pet.species}, Breed: {current_pet.breed}, Age: {current_pet.age}"
        )
        print("-----------------------------------")


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


def select_pet(current_user):
    print("Here is a list of your pets: ")
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

    return pet_choice


def update_pet(current_user):
    os.system("cls" if os.name == "nt" else "clear")
    print("Pets R Us - Update Pet")
    print("Lets get fido updated!")
    print("Which pet would you like to update?")

    get_pet = current_user.pets[select_pet(current_user)]

    for field in get_pet.__table__.columns.keys():
        if field in ["id", "owner_id"]:
            continue

        current_value = getattr(get_pet, field)
        new_value = input(f"Enter new {field} (current: {current_value}): ")
        if new_value:
            setattr(get_pet, field, new_value)

    print("Updating pet info...")
    session.commit()
    print("Pet info updated successfully!")
    return


def delete_pet(current_user):
    os.system("cls" if os.name == "nt" else "clear")
    print("Pets R Us - Delete Pet")
    print("Poor fido... Goodbye old friend.")
    print("What pet would you like to delete?")

    get_pet = current_user.pets[select_pet(current_user)]
    print("Are you sure you want to delete this pet?")
    answer = input("(yes/no): ")
    if answer == "no":
        print("Phew! That was close!")
        return
    elif answer == "yes":
        print("Deleting pet...")
        session.delete(get_pet)
        session.commit()
        print("Pet deleted successfully!")
        return
    else:
        print("Oops! Thats not a valid number. Please try again.")
        delete_pet(current_user)  # Recursion for invalid input
