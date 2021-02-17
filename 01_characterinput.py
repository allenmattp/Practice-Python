from datetime import datetime

def main():
    YEAR = datetime.now().year
    calc = 0
    name = input("Please enter your name:")
    age = input("Please enter your age:")
    n = input("How many copies of the message do you want to see?")

    try:
        calc = (100-int(age)) + YEAR
        for i in range(int(n)):
            print("Hi", name + "!", "You will be 100 in the year", calc)
    except ValueError:
        # Error, can't turn what they typed into a number
        print("Please enter whole numbers! Let's start over...")
        main()

if __name__ == "__main__":
    main()