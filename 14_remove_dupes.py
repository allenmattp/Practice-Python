"""
Write a program that takes a list and returns a new list
that contains all the elements of the first list minus all the duplicates.
"""

import random

def main():
    def remove_dupes(list):
        # complete with set
        set_list = set(list)

        # complete with loop
        loop_list = []
        for i in list:
            if i not in loop_list:
                loop_list.append(i)

        # sort the loop list so it's easier to compare to set
        loop_list.sort()
        # return each list
        return set_list, loop_list

    random_list = [random.randrange(10) for x in range(10)]

    print(remove_dupes(random_list))

if __name__ == '__main__':
    main()