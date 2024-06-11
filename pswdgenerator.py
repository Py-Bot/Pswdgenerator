import string
import random

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    char_pool = ''
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character type must be selected")

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the password generator!")
    length = int(input("Enter the desired length of the password: "))
    use_uppercase = input("Use capital letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Use lower case letters? (y/n): ").lower() == 'y'
    use_digits = input("Use numbers? (y/n): ").lower() == 'y'
    use_special = input("Use special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"Your generated password is: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
