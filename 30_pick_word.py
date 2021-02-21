"""
write a function that picks a random word from a list of words from the SOWPODS dictionary.
"""
import random


def main(file_name):
    with open(file_name, "r") as file:
        words = file.read().splitlines()
        print(words[random.randrange(len(words))])
    file.close()


if __name__ == '__main__':
    main("sowpods.txt")