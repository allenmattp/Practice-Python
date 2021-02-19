"""
Given a .txt file that has a list of files corresponding to the
SUN database scene recognition database,
and lists the file directory hierarchy for the images.
count how many of each “category” of each image there are.,
and print out the results to the screen.
"""


def main(file_name):
    with open(file_name, "r") as file:
        line = file.readline()
        cat_list = []
        while line:
            cat = line.split("/")
            line = file.readline()
            cat_list.append(cat[2])
        cat_set = set(cat_list)
        cat_dict = {}
        # Creates a dictionary so count of each category can be easily looked up
        for cat in cat_set:
            cat_dict[cat] = cat_list.count(cat)
        print("Categories:")
        [print(c) for c in cat_set]
        print("Total categories: ", len(cat_set))
    file.close()


if __name__ == '__main__':
    main("Training_01.txt")
