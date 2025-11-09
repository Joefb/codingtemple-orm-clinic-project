from models import (
    Owners,
    session,
)


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


def register(owner_info):
    try:
        check_email = (
            session.query(Owners).where(Owners.email == owner_info["email"]).first()
        )

        if check_email:
            return "Registration failed: Email already in use."

        else:
            new_owner = Owners(**owner_info)
            session.add(new_owner)
            session.commit()
            print("Registration successful!")
            return new_owner

    except Exception as e:
        return f"Registration failed: {e}"
