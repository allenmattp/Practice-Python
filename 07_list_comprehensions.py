"""
Write one line of Python that takes this list a
and makes a new list that has only the even elements of this list in it.
"""
import random

def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    list = [random.randrange(1,3) for x in range(random.randrange(10))]
    even_a = [x for x in a if not x % 2]
    even_list = [x for x in list if not x % 2]
    print(even_a)
    print(even_list)

if __name__ == "__main__":
    main()