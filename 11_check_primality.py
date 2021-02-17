"""
Ask the user for a number and determine whether the number is prime or not.
"""

def main():
    try:
        user_num = int(input("Choose a number:"))
        # Add a neg sign on message if user enters neg number
        is_neg = ""
        if user_num < 0:
            user_num *= -1
            is_neg = "-"
        # Edge cases for 0 and 1 (and -1)
        if not user_num or user_num == 1:
            print(is_neg + str(user_num), "is not a prime number because math.")
        for i in range(1, user_num):
            if not user_num % i and i > 1:
                print(i, "is a divisor of", user_num)
                print("Ergo,", is_neg + str(user_num), "is not a prime number.")
                break
            elif i >= user_num - 1:
                print(is_neg + str(user_num), "is a prime number.")
    except ValueError:
        # Error, can't turn input into a number
        print("Please enter a whole number! Let's start over...")
        main()

if __name__ == "__main__":
    main()