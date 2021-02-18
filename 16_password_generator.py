from random_words import RandomWords
import random


def main():
    # variables storing characters for password generation
    r = RandomWords()                           # import string <-- alternate (easier) method
    low_alpha = "abcdefghijklmnopqrstuvwxyz"    # string.ascii_lowercase
    cap_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    # string.ascii_uppercase
    numbers = "0123456789"                      # string.digits
    special_chars = "~!@#$%^&*()_+"             # string.punctuation
    words = r.random_words()

    def create_password():
        print("This program will create a password.")
        pw_length = input("Type 'easy' for quick password, otherwise type desired password length. ")

        password = ""

        # Creates an easy password if user enters 'easy' anywhere in their input
        if "easy" in pw_length.lower():
            # Easy password is an English word with a number
            password = words[random.randrange(len(words))] + str(random.randrange(100))

        else:
            try:
                # If user entered an integer create random password
                for i in range(int(pw_length)):
                    char_type = random.randrange(4)
                    if not char_type:
                        password += low_alpha[random.randrange(len(low_alpha))]
                    elif char_type == 1:
                        password += cap_alpha[random.randrange(len(cap_alpha))]
                    elif char_type == 2:
                        password += numbers[random.randrange(len(numbers))]
                    else:
                        password += special_chars[random.randrange(len(special_chars))]
            except ValueError:
                # Error, can't turn input into a number
                print("Please enter length as a whole number! Let's start over...")
                create_password()
        return password

    print("Your password:", create_password())


if __name__ == '__main__':
    main()
