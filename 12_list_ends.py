"""
Write a program that takes a list of numbers
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""
import random

def main():
    # Create a random list
    list_test = [random.randrange(1,100) for i in range(random.randrange(11))]
    print("List:", list_test)

    def list_ends(list):
        if len(list) > 1:
            return list[0], list[-1]
        else:
            return list

    print("Result:", list_ends(list_test))

if __name__ == "__main__":
    main()