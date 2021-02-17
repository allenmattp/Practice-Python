"""
Ask the user for a number and determine whether the number is prime or not.
"""

def main():
    try:
        user_num = int(input("Choose a number:"))
        for i in range(2, user_num):
            if not user_num % i:
                print(i, "is a divisor of", user_num)
                print("Ergo,", user_num, "is not prime.")
                break
            elif i >= user_num - 1:
                print(user_num, "is a prime number.")
    except ValueError:
        # Error, can't turn input into a number
        print("Please enter a whole number! Let's start over...")
        main()

if __name__ == "__main__":
    main()