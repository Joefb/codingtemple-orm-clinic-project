from models import Owners, Pets, Vets, session, Appointments
from bp_pets import view_pets, select_pet
from datetime import datetime
import os


def new_appointment(current_user):
    os.system("cls" if os.name == "nt" else "clear")
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
    date_format = "%Y-%m-%d"
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
    os.system("cls" if os.name == "nt" else "clear")
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
    print("-----------------------------------")

    for pet in current_user.pets:
        print(f"Appointments for {pet.name}:")
        for appointment in pet.appointments:
            print(
                f"ID: {appointment.id}\nDate: {appointment.appointment_date}\nVet: {appointment.vet.name}\nStatus: {appointment.status}\nNotes: {appointment.notes}\nStatus: {appointment.status}"
            )
        print("-----------------------------------")


def reschedule_appointment(current_user):
    os.system("cls" if os.name == "nt" else "clear")
    print("Pets R Us - Reschedule Appointment")
    print("Pulling up your appointments...")
    view_appointments(current_user)
    print("What appointment? Use the ID number.")

    while True:
        try:
            id_input = int(input("Enter appointment ID: "))
            select_appointment = (
                session.query(Appointments).filter_by(id=id_input).first()
            )

            if not select_appointment:
                print("Oops! Try that again. Thats not a valid ID.")
                continue

            elif select_appointment:
                new_date = get_date()
                select_appointment.appointment_date = new_date
                session.commit()
                print("Appointment rescheduled successfully!")
                return

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue


def complete_appointment(current_user):
    os.system("cls" if os.name == "nt" else "clear")
    print("Pets R Us - Complete Appointment")
    view_appointments(current_user)
    print("Which appointment would you like to mark as complete? Use the ID number.")

    while True:
        try:
            id_input = int(input("Enter appointment ID: "))
            select_appointment = (
                session.query(Appointments).filter_by(id=id_input).first()
            )

            if not select_appointment:
                print("O snap!! Try that again. Thats not a valid ID.")
                continue

            elif select_appointment:
                select_appointment.status = "Complete"
                session.commit()
                print("Appointment marked as complete successfully!")
                return

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
