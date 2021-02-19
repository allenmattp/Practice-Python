"""
Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to largest)
and another number.
The function decides whether or not the given number is inside the list
and returns (then prints) an appropriate boolean.
"""

import random

test_list = [x for x in range(100)]


def search(elem, list):
    # iterate through list until element is found
    if elem in list:
        print("True")
        return True
    # return False if element not in list
    else:
        print("False")
        return False

def binary_search(elem, list):
    # begin search at middle of the list
    mid_pos = len(list) // 2
    while mid_pos:
        mid_pos = len(list) // 2
        # return true if element found
        if list[mid_pos] == elem:
            print(True)
            return True
        # if middle of list is
        elif list[mid_pos] > elem:
            list = list[:mid_pos]
        elif list[mid_pos] < elem:
            list = list[mid_pos:]
    print("False")
    return False

if __name__ == '__main__':
    rand_num = random.randrange(200)
    print("Linear:")
    search(rand_num, test_list)
    print("Binary:")
    binary_search(rand_num, test_list)