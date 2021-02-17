"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
"""

def main():
    try:
        user_num = int(input("Choose a number:"))
        for i in range(1, user_num + 1):
            if not user_num % i:
                print(i, "is a divisor of", user_num)
    except ValueError:
        # Error, can't turn input into a number
        print("Please enter a whole number! Let's start over...")
        main()

if __name__ == "__main__":
    main()