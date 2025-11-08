# Project: ORM Clinic Project

## Cloning the repository and setting up the environment

- Clone the following repository: <https://github.com/AllanSaleh/ORM-Clinic-Project-Assignment.git>
- git clone <https://github.com/AllanSaleh/ORM-Clinic-Project-Assignment.git>
- Open vs code to the folder that it creates (delete the .git folder from the folder it creates)

### Create your virtual environment

- windows: python -m venv venv
- mac: python3 -m venv venv

### Activate your virtual environment

- windows: venv\Script\activate
- mac: source venv/bin/activate

### Install SQLAlchemy

- pip install sqlalchemy

### Add .gitignore file to ignore the venv folder

- .gitignore venv

### Save your dependencies to requirements.txt

- pip freeze > requirements.txt
