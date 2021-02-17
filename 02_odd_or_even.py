"""
Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
"""
def main():

    try:
        number = int(input("Enter a number:"))
        if not number % 4:
            print("Divisible by 4")
        elif number % 2:
            print("ODD")
        else:
            print("EVEN")

    except ValueError:
        # Error, can't turn input into a number
        print("Please enter whole numbers! Let's start over...")
        main()

"""
Ask the user for two numbers: 
one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.
"""
def bonus():
    try:
        num = int(input("Enter a number:"))
        check = int(input("Divisor check:"))
        if not num % check:
            print(num, "is divisible by", check)
        else:
            print(num, "is NOT divisible by", check)
    except ValueError:
        # Error, can't turn input into a number
        print("Please enter whole numbers! Let's start over...")
        bonus()

if __name__ == "__main__":
    main()
    bonus()