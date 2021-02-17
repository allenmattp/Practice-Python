"""
Ask the user for a string and print out whether this string is a palindrome or not.
"""

def main():
    try:
        entry = str(input("Palindrome check:"))
        entry_list = []
        check = []
        # Make user's string into list
        for char in range(len(entry)):
            # ignore spaces/punctuation
            if entry[char].isalpha():
                entry_list.append(entry[char].lower())

        # Create backwards list of user's string
        for char in range(len(entry)):
            if entry[-char-1].isalpha():
                check.append(entry[-char-1].lower())

        if entry_list == check:
            print("It is a palindrome!")
        else:
            print("It is NOT a palindrome")
    except ValueError:
        # Error, can't turn input into a number
        print("Unreadable entry. Try again!")
        main()

if __name__ == "__main__":
    main()