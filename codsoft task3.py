import string

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    return strength

def main():
    print("Welcome to the Password Checker!")
    print("Please follow the instructions below to check the strength of your password:")
    print("1. Your password should be at least 6 characters long.")
    print("2. It should include a mix of uppercase and lowercase letters, numbers, and special characters.")
    print("3. Avoid using easily guessable information, such as your name or common words.")
    print("4. Consider using a passphrase or a combination of unrelated words for added security.")

    try:
        password = input("Enter your password: ")
        if len(password) < 6:
            print("Password should be at least 6 characters long.")
            return

        strength = check_password_strength(password)
        if strength == 4:
            print("Password Strength: Strong\n Your Password is :", password)
        elif strength >= 2:
            print("Password Strength: Medium\n Your Password is :", password)
        else:
            print("Password Strength: Weak\n Your Password is :", password)

    except ValueError:
        print("Invalid input. Please enter a valid password.")

if __name__ == "__main__":
    main()
