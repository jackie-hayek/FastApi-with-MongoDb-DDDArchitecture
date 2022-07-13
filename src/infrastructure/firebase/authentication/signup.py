from src.infrastructure.firebase.configuation.config import auth, db

email = input("Enter your email: ")
password = input("Enter your password: ")
confirm_pass = input("Confirm your password: ")

created = False

if password == confirm_pass:
    try:
        auth.create_user_with_email_and_password(email, password)
        print("Success!")
        created = True
    except:
        print("Email already exists")

if created:
    try:
        data = {'email': email, 'password': password, 'active': True}
        db.child("users").push(data)
        print("User is added to the database")
    except:
        print("User not added to the database")
