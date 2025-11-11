from models import Owners, Pets, Vets, session, Appointments
from bp_pets import view_pets, select_pet
from datetime import datetime

# IMPORTANT when creating an appointment, it is required to convert the date string
# "YYYY-MM-DD" int a python date object

# date_format = "%Y-%m-%d"  # This will be used to format your date

# Syntax for date conversion

# new_date = datetime.strptime("Date String", date_format)
# example
# today = datetime.strptime("2025-08-08", date_format)


def new_appointment(current_user):
    print("Pets R Us - Create New Appointment")
    print("-----------------------------------")
    print("What pet would you like to schedule an appointment for?")
    get_pet = current_user.pets[select_pet(current_user)]
    get_vet = show_vets()
    set_date = get_date()
    set_note = get_notes()

    new_appointment = Appointments()
    new_appointment.pet_id = get_pet.id
    new_appointment.veterinarian_id = get_vet.id
    new_appointment.appointment_date = set_date
    new_appointment.notes = set_note
    session.add(new_appointment)
    session.commit()


def get_notes():
    print("What notes would you like to add for the appointment?")
    input_notes = input("Enter notes (or leave blank): ")
    return input_notes


def get_date():
    date_format = "%Y-%m-%d"  # This will be used to format your date
    print("What date would you like to schedule the appointment for?")

    while True:
        get_date_input = input("Please enter the date in YYYY-MM-DD format: ")
        if not get_date_input:
            print("Date cannot be empty. Please try again.")
            continue

        try:
            set_date = datetime.strptime(get_date_input, date_format)
            return set_date
        except ValueError:
            print("Invalid date format. The date format must be YYYY-MM-DD.")


def show_vets():
    print("Please select a veterinarian for the appointment:")
    print("Here is a list of our available veterinarians:")
    print("-----------------------------------")

    vets = session.query(Vets).all()
    for vet in vets:
        print(
            f"Employee Number: {vet.id} - Name: {vet.name} - Specialization: {vet.specialization}"
        )
        print("-----------------------------------")

    while True:
        try:
            vet_id = int(input("Enter the vet employee number: "))

            selected_vet = session.query(Vets).filter_by(id=vet_id).first()
            if not selected_vet:
                print("Invalid employee number. Please try again.")
            elif selected_vet:
                return selected_vet

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def view_appointments(current_user):
    print("Pets R Us - View Appointments")
    print("Hooray! We get to see you soon..........")
    print("-----------------------------------")

    for pet in current_user.pets:
        print(f"Appointments for {pet.name}:")
        for appointment in pet.appointments:
            print(
                f"Date: {appointment.appointment_date}\nVet: {appointment.vet.name}\nStatus: {appointment.status}\nNotes: {appointment.notes}"
            )
        print("-----------------------------------")


# Reschedule appointments
# Show appointments with ids (Loop over current user pets, loop over each pets appointments e.g nested loop)
# Select an appointment by id
# ask user for new date
# convert date
# update the appointment date

# Complete appointments
# Show appointments with ids (Loop over current user pets, loop over each pets appointments e.g nested loop)
# query the appointment by id
# change appointment.status to 'complete"
# print success message
