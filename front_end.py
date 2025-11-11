# DONT FORGET TO IMPORT FUNCTIONS AFTER YOU MAKE THEM
from bp_auth import login, register
from bp_owner import display_profile, update_profile, delete_profile
from bp_pets import view_pets, create_pet, update_pet, delete_pet
from bp_appointments import (
    new_appointment,
    view_appointments,
    reschedule_appointment,
    complete_appointment,
)
from models import session

# from bp_appointments import
import os


def welcome_menu():
    owner = None

    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("""
--------- Welcome to Pets R Us ------------------------
    Where we love your pets so you don't have to!
--------------------------------------------------------
        1.) Login
        2.) Register
""")
        choice = input("select (1 or 2) or 'quit': ")
        if choice == "quit":
            print("Thanks for visiting Pets R Us!")
            print(
                "Own a Ford? Sorry to hear that! Donate that piece of shit and adopt a pet instead!"
            )
            print("Call for more details!")
            exit()

        if choice == "1":
            owner = owner_login()
            if owner:
                return owner

        elif choice == "2":
            owner = owner_register()
            if owner:
                return owner

        else:
            print("Invalid response please try again.")


def owner_login():
    credentials = {"email": "", "password": ""}
    os.system("cls" if os.name == "nt" else "clear")
    print("Pets R Us Login!:")

    for key in credentials:
        credentials[key] = input(f"Enter your {key.title()}: ")

    owner = login(credentials)

    if isinstance(owner, str):
        print(owner)
        return None
    else:
        return owner


def owner_register():
    owner_info = {"name": "", "phone": "", "email": "", "password": ""}
    os.system("cls" if os.name == "nt" else "clear")
    print("Pets R Us Registration:")
    print("Woof Woof! Chirp Chirp! Meow Meow!")

    for key in owner_info:
        owner_info[key] = input(f"Enter your {key.title()}: ")

    new_owner = register(owner_info)

    if isinstance(new_owner, str):
        print(new_owner)
        return None
    else:
        return new_owner


def owner_menu(current_user):
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("""
    1.) View Profile
    2.) Update Profile
    3.) Delete Profile
    4.) Back""")
        choice = input("choose 1-3: ")
        if choice == "1":
            display_profile(current_user)

        elif choice == "2":
            current_user = update_profile(current_user)

        elif choice == "3":
            if delete_profile(current_user):
                main()
            else:
                main()

        elif choice == "4":
            return
        else:
            print("Invalid Selection.")


def pets_menu(current_user):
    os.system("cls" if os.name == "nt" else "clear")

    while True:
        print("""
1.) View my Pets
2.) Create Pet
3.) Update Pet
4.) Delete Pet
5.) Back""")
        choice = input("choose 1-5: ")
        if choice == "1":
            view_pets(current_user)

        elif choice == "2":
            create_pet(current_user)

        elif choice == "3":
            update_pet(current_user)

        elif choice == "4":
            delete_pet(current_user)

        elif choice == "5":
            return
        else:
            print("Invalid Selection.")


def appointments_menu(current_user):
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("""
1.) Schedule appointment
2.) View appointments
3.) Reschdule appointment
4.) Complete appointment
5.) Back
""")
        choice = input("choose 1-5: ")
        if choice == "1":
            new_appointment(current_user)

        elif choice == "2":
            view_appointments(current_user)

        elif choice == "3":
            reschedule_appointment(current_user)

        elif choice == "4":
            complete_appointment(current_user)

        elif choice == "5":
            return


def logout(current_user):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Goodbye {current_user.name.title()}!")
    print("Thanks for visiting Pets R Us!")
    print(
        "Dont forget our weekly special. Put one pet down get another pet put down free!(Pugs are always free!)"
    )
    print("Visit us again to take care of your furry friends! Woof Woof!")
    session.close()
    exit()


def main():
    current_user = welcome_menu()

    os.system("cls" if os.name == "nt" else "clear")
    if current_user:
        while True:
            print("""
        --------- Pet Clinic --------
        1.) Manage Profile
        2.) My Pets
        3.) My Appointments
        4.) Logout
        """)
            choice = input("choose 1-3: ")
            if choice == "4":
                logout(current_user)
            elif choice == "1":
                owner_menu(current_user)
            elif choice == "2":
                pets_menu(current_user)
            elif choice == "3":
                appointments_menu(current_user)
            else:
                print("Invalid Selection.")


main()
