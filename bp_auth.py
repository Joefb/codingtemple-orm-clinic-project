from models import (
    Owners,
    session,
)  # Need the Users model to create and search for users
# need the sesssion to add users to our db


# Create engine
# engine = create_engine("sqlite:///clinic.db", echo=True)
# Create Base instance
# Base = declarative_base()


def login(credentials):
    try:
        owner = (
            session.query(Owners).where(Owners.email == credentials["email"]).first()
        )
        if owner and owner.password == credentials["password"]:
            return owner
        else:
            return "Login failed: Invalid email or password."

    except Exception as e:
        return f"An error occurred during login: {e}"


def register():
    # Create Register function
    # get all info required to create an owner from the user
    # try and create an Owner from the info (will fail if email is already in user)
    # if you succeed return user
    # except error and print message
    pass
