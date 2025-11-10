from models import Owners, session

# from front_end import main
import os


def display_profile(current_user):
    os.system("cls" if os.name == "nt" else "clear")
    print("Pets R Us - View Profile")
    print("Hisssss! Bark! Chirp!")
    print("\n--- Your Profile Information ---")
    print(f"Name: {current_user.name}")
    print(f"Phone: {current_user.phone}")
    print(f"Email: {current_user.email}")
    print("---------------------------\n")
    return


def update_profile(current_user):
    os.system("cls" if os.name == "nt" else "clear")
    print("Pets R Us - Update Profile")
    print("\n--- Current Profile Information ---")
    print(f"1. Name: {current_user.name}")
    print(f"2. Phone: {current_user.phone}")
    print(f"3. Email: {current_user.email}")
    print("---------------------------\n")

    fields = {"1": "name", "2": "phone", "3": "email"}

    choice = input(
        "What would you like to update my pet loving friend?(or type 'done'): "
    )
    while choice != "done":
        if choice in fields:
            new_value = input(f"Enter new {fields[choice].title()}: ")
            setattr(current_user, fields[choice], new_value)
            session.commit()
            print(f"{fields[choice].title()} updated successfully!")
        else:
            print("Is your cat on the keyboard again? Please try again.")

        choice = input(
            "What would you like to update my pet loving friend?(or 'done'): "
        )

    print("\n--- Updated Profile Information ---")
    print(f"Name: {current_user.name}")
    print(f"Phone: {current_user.phone}")
    print(f"Email: {current_user.email}")
    print("---------------------------\n")
    return current_user


def delete_profile(current_user):
    os.system("cls" if os.name == "nt" else "clear")
    print("Pets R Us - Delete Profile")
    print("Awweeee so sad.... Hisssss! Bark! Chirp! Poop.")

    confirm = input("Are you sure you want to delete your profile?(yes/no): ")
    if confirm.lower() == "yes":
        session.delete(current_user)
        session.commit()
        print(
            "Your profile has been deleted. We're sad to see you go!(not really. your pet pooped on my favorite scarf...)"
        )
        print(
            "Hahaha! We dont delete anything! Selling your private data to the highest.... naaaa lowest bidder!"
        )

        # Restart the app
        return True

    elif confirm.lower() == "no":
        print("Glad you decided to stay! Returning to main menu.")
        return False
    else:
        # Oooo slip in some recussion
        delete_profile(current_user)


# Update profile function
# Ask user to confirm they want to delete
# if so delete the current user from the session
# commits changes
# call main() to start the program over

