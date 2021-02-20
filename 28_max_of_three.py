"""
Implement a function that takes as input three variables, and returns the largest of the three.
Do this without using the Python max() function!
"""
import random


def find_max(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

if __name__ == '__main__':
    x = round(random.random()*100, 2)
    y = round(random.random()*100, 2)
    z = round(random.random()*100, 2)
    print(x, y, z)
    print(find_max(x, y, z))