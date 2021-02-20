"""
Given two .txt files that have lists of numbers in them,
find the numbers that are overlapping.
"""


def main(file_one, file_two):
    with open(file_one, "r") as f1, open (file_two) as f2:
        l1 = f1.read().splitlines()
        l2 = f2.read().splitlines()
        overlap = [l for l in l1 if l in l2]
        print(overlap)

    f1.close()
    f2.close()


if __name__ == '__main__':
    main("primenumbers.txt", "happynumbers.txt")
