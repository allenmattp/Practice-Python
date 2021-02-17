"""
Take two lists and write a program that returns a list
that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
"""
import random

def main():
    # Create two random lists
    list_a = [random.randrange(1,100) for i in range(random.randrange(10,101))]
    list_b = [random.randrange(1,100) for i in range(random.randrange(10,101))]
    print("A:", list_a)
    print("B:", list_b)
    # Create list to show what elements appear in both lists
    list_both = []
    # Compare lists and print which elements appear in both (no duplicates)
    for i in range(len(list_a)):
        if list_a[i] in list_b and list_a[i] not in list_both:
            list_both.append(list_a[i])
    print("Common elements:", list_both)

if __name__ == "__main__":
    main()