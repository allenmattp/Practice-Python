"""
Take a list and print out all elements of the list that are less than 5
"""
import random

def main():
    # Create list with random content
    list = []
    for i in range(100):
        list.append(random.randrange(100))

    new_list = []
    user_n = int(input("Enter number:"))
    for e in range(len(list)):
        if list[e] <= user_n:
            new_list.append(list[e])
    print(new_list)

if __name__ == "__main__":
    main()