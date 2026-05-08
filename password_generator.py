import random
import string


def generate_password(length, mode):
    if mode == "1":
        characters = string.ascii_letters

    elif mode == "2":
        characters = string.ascii_letters + string.digits

    elif mode == "3":
        characters = string.ascii_letters + string.digits + string.punctuation

    else:
        return None

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


def main():
    print("\n--- Password Generator ---")
    print("1. Letters Only")
    print("2. Letters + Numbers")
    print("3. Strong Password (Symbols Included)")

    mode = input("Choose password type: ")

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Please enter a valid number.")
            return

        password = generate_password(length, mode)

        if password:
            print("\nGenerated Password:")
            print(password)
        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter numbers only.")


main()