from database import database

def add_user_to_database(school, email, password, location):
    if email not in database:
        # Auto-increment the ID
        user_id = len(database) + 1

        # Add the user to the database
        database[email] = {
            'id': user_id,
            'school': school,
            'email': email,
            'password': password,
            'location': location
        }
        print(f"User with email '{email}' successfully added.")
    else:
        print(f"User with email '{email}' already exists in the database.")
