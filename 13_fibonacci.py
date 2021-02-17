"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
"""

def main():
    try:
        num = int(input("How many Fibonnaci numbers should we generate? "))

        # track two variables: the current and previous number
        current = 1
        previous = 1
        # store numbers in a list; if user enters <= 0 returns 0
        list = [0]
        for i in range(num):
            # First number in sequence (after 0) is 1
            if not i:
                list.append(current)
            # Second number in sequence is also 1
            elif i == 1:
                list.append(current)
            else:
                # find current value by adding previous value
                current += previous
                # set value for previous so it's ready for next iteration
                previous = current - previous
                list.append(current)
        print("All numbers:", list)
        print("Last number:", list[-1])
    except ValueError:
        # Error, can't turn input into a number
        print("Please enter a whole number! Let's start over...")
        main()

if __name__ == '__main__':
    main()