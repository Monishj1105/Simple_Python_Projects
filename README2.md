# 🔐 Password Generator 🔐

## Overview

This Python script generates a secure, random password based on user-specified length. It uses a mix of lowercase letters, uppercase letters, digits, and special characters to create strong passwords suitable for enhancing online security.

## Features

- **Random Password Generation:** Ensures unpredictability in the generated password.
- **Customizable Length:** Users can specify the desired length of the password.
- **Input Validation:** Checks for valid numeric input and enforces minimum and maximum length constraints.
- **Secure Character Set:** Includes a comprehensive set of characters for stronger password security.

## Requirements

- Python 3.x
- No external libraries are required; only the standard `random` module is used.

## How It Works

1. The script prompts the user to enter the desired password length.
2. It validates the input to ensure it's a numeric value and within the allowed range.
3. It generates a password using `random.sample()`, which selects unique characters from the defined character set.
4. The password is displayed to the user.

## Usage

### Step 1: Run the Script

```bash
python password_generator.py
```

### Step 2: Enter Password Length

You'll be prompted to enter the desired password length:

```
🔐 Welcome to the Password Generator! 🔐
Enter the length of the password (minimum 1):
```

- **Valid Input:** Enter a number between 1 and 78 (since the character set has 78 unique characters).
- **Invalid Input:** If you enter a non-numeric value or a number outside the valid range, the script will display an error message.

### Example Output

```
🔐 Welcome to the Password Generator! 🔐
Enter the length of the password (minimum 1): 12
✅ Your secure password is: d3!G@7bZ#1k
```

## Example Code

```python
import random  # Importing the random module to generate random selections

# Defining the character set for the password
password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?"

# Welcome message
print("🔐 Welcome to the Password Generator! 🔐")

# Prompt for password length
try:
    length_password = int(input("Enter the length of the password (minimum 1): "))

    # Input validation
    if length_password < 1:
        print("❌ Password length must be at least 1 character.")
    elif length_password > len(password_characters):
        print(f"❌ Password length cannot exceed {len(password_characters)} characters.")
    else:
        # Generate and display password
        password = "".join(random.sample(password_characters, length_password))
        print(f"✅ Your secure password is: {password}")
except ValueError:
    print("❌ Invalid input! Please enter a numeric value for the password length.")
```

## Notes

- **Uniqueness:** The script ensures no repeated characters within the password. If you require passwords with repeated characters, consider using `random.choices()` instead of `random.sample()`.
- **Security:** Although this generates strong passwords, for high-security applications, consider using Python’s `secrets` module for cryptographically secure random numbers.

## License

This project is licensed under the MIT License. Feel free to modify and use it as needed.

---
