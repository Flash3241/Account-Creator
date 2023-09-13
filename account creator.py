import re
import random
import string

def generate_random_password(length=12):
    # Generate a random password with the specified length
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Dictionary to store accounts (email as the key and password as the value)
accounts = {}

while True:
    choice = input('Do you want to (1) Sign Up or (2) Log In? Enter 1 or 2: ')
    
    if choice == '1':
        while True:
            email = input('Enter your Email: ')
            
            if not re.match(r'^\S+@\S+\.\S+$', email):
                print('Invalid email format')
            elif email in accounts:
                print('Email already exists. Please choose a different email.')
            else:
                print('Email is valid')
                break
        
        while True:
            password = input('Enter a Password: ')
        
            if len(password) < 10:
                print('Password must be at least 10 characters')
            elif not any(char.isdigit() for char in password):
                print('Password must contain at least one number')
            elif not re.search("[!@#$%^&*()_+{}:;<>,.?~]", password):
                print('Password must contain at least one special character')
            else:
                # Store the account in the dictionary
                accounts[email] = password
                print('Account created successfully!')
                break
    elif choice == '2':
        login_email = input('Enter your Email for login: ')

        if login_email not in accounts:
            print('Email not used. Suggest signing up')
            continue
        login_password = input('Enter your Password for login: ')
        
        if login_email in accounts and accounts[login_email] == login_password:
            print('Login successful!')
            break
        else:
            print('Invalid password. Please try again.')
    else:
        print('Invalid choice. Please enter 1 to Sign Up or 2 to Log In.')