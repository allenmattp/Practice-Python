"""
Take two lists and write a program that returns a list
that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
USE LIST COMPREHENSION
"""
import random

def main():
    # Create two random lists
    list_a = [random.randrange(1,101) for i in range(random.randrange(10,101))]
    list_b = [random.randrange(1,101) for i in range(random.randrange(10,101))]
    # Create list to show what elements appear in both lists
    # Use set to avoid duplicates
    list_both = set([elem for elem in list_a if elem in list_b])
    print("Common elements:", list_both)

if __name__ == "__main__":
    main()