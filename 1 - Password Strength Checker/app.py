import string

special_chars = string.punctuation
print(special_chars)

"""
Password length (minimum of 8 characters).
Contains at least one lowercase letter, one uppercase letter, one digit, and one special character.
Should not contain common dictionary words like "password", "123456", "admin", etc.
"""
def check_strength(password):

    # Criteria 1
    if len(password) < 8:
        return "Weak"
    
    # Criteria 2
    if not any(char.islower() for char in password):
        return "Weak"
    if not any(char.isupper() for char in password):
        return "Weak"
    if not any(char.isdigit() for char in password):
        return "Weak"
    
    # Criteria 3
    with open('/home/kali/Desktop/Python - Red Team Assignment 1/1 - Password Strength Checker/dictionary.txt', 'r') as file:
        dictionary = file.read().splitlines()

        if any(word in password for word in dictionary):
            return "Weak"
        
    # Strong
    if any(char in special_chars for char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
        return "Strong"

    # Moderate
    if any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
        return "Moderate"

def main():
    password = input("Enter password: ")
    strength = check_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()