import random  # Importing the random module to generate random selections

# Defining the character set for the password, including lowercase, uppercase, digits, and special characters
password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?"

# Welcome message for the user
print("🔐 Welcome to the Password Generator! 🔐")

# Asking the user to input the desired length of the password
try:
    length_password = int(input("Enter the length of the password (minimum 1): "))

    # Input validation: Check if the length is greater than 0
    if length_password < 1:
        print("❌ Password length must be at least 1 character.")
    elif length_password > len(password_characters):
        print(f"❌ Password length cannot exceed {len(password_characters)} characters.")
    else:
        # Generating the password using random.sample to ensure unique characters
        password = "".join(random.sample(password_characters, length_password))
        
        # Displaying the generated password
        print(f"✅ Your secure password is: {password}")
except ValueError:
    print("❌ Invalid input! Please enter a numeric value for the password length.")
