from signup import add_user_to_database

# Function to simulate front-end input
def sign_up_user(school, email, password, location):
    add_user_to_database(school, email, password, location)

# Example sign-ups
sign_up_user("School A", "user1@example.com", "password1", "Location A")
sign_up_user("School B", "user2@example.com", "password2", "Location B")
sign_up_user("School A", "user1@example.com", "password1", "Location A")
