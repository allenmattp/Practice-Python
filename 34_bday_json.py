"""
Modify your program from Part 1 to load the birthday dictionary from a JSON file on disk,
rather than having the dictionary defined in the program.

note: run create_json() function to generate a file
pulls data from http://www.indepthinfo.com/articles/presidential-birthdays.shtml (no affiliation)
"""


from bs4 import BeautifulSoup
import requests
import json


def main():
    """
    Runs program. User can choose action by entering an integer.
    """
    # create_json()                     # uncomment this line to start with the default JSON file first
    file="info.json"
    done = False
    while not done:
        try:
            print("\nWelcome to the Presidential Birthday Lookup Service.")
            operation = int(input("\nDo you want to:\n"
                              "1. Enter a new birthday\n"
                              "2. Look up a birthday\n"
                              "3. Print all Presidents\n"
                              "4. Quit\n"
                              "(enter a number)\n"))
            if operation == 1:
                write_bday(file)
            elif operation == 2:
                get_bday(read_json(file))
            elif operation == 3:
                print_all_names(read_json(file))
            elif operation == 4:
                print("Goodbye.")
                done = True
        except ValueError:
            print("Enter a number to make your selection.")


def read_json(file):
    """
    reads a JSON file and returns its data
    :param file: JSON file
    :return: JSON data
    """
    with open(file, "r") as f:
        bday_json = json.load(f)
    return bday_json


def get_bday(json):
    """
    Prints a birthday based on user input (search by name).
    Runs until a name is found
    :param json: DATA not file. use read_json(file) to read a file if necessary
    """
    done = False
    while not done:
        name = input("Enter a President's full name (eg Thomas Jefferson): ")
        for p in json["presidents"]:
            if name in p["name"]:
                print("{}'s birthday is {}.".format(p["name"], p["birthday"]))
                done = True
        if not done:
            print("No matches found. Try again.")


def write_bday(file):
    """
    takes user's input and adds new entry with name + birthday
    :param file: existing JSON file
    """
    with open(file, "r") as f:
        data = json.load(f)                 # load JSON file
        temp = data["presidents"]           # get current list of presidents

        name = input("Name: ")              # user enters name
        birthday = input("Birthday: ")      # user enters birthday
        new_entry = {"name": name,
                     "birthday": birthday
                     }
        temp.append(new_entry)              # add to list
        data["presidents"] = temp           # update data
    f.close()

    with open(file, "w") as f:

        json.dump(data, f)                  # rewrite file
    f.close()


def print_all_names(json):
    """ Prints all names in the JSON file"""
    for p in json["presidents"]:
        print(p["name"])


def create_json():
    """
    Runs get_bday_list with a dictionary of President birthdays
    """
    birthdays = "http://www.indepthinfo.com/articles/presidential-birthdays.shtml"
    bday_list = get_bday_list(birthdays)
    gen_bday_json(bday_list)


def get_bday_list(url):
    """
    Pulls presidential birthdays from website and cleans data for this task
    :param url: website that has table of birthdays
    :return: cleaned list of names/birthdays
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    cols = soup.find_all("td")
    bday_list = []
    for col in cols:
        bday_list.append(col.text.strip())
    bday_list = bday_list[7:-3]
    return bday_list


def gen_bday_json(list):
    """
    Creates a json file of Presidents birthdays where
    each president has attributes name, birthday
    :param list: expects [key1, value1, key2, value2,...,key_n, value_n] format
    """
    bday_list = []                          # list of presidents
    bday_dict = {}                          # dictionary containing name/birthday for a president
    for index, item in enumerate(list):     # goes through list and creates entries for each president
        if index % 2 == 0:                  # "name" is in even index space
            bday_dict = {"name": item}      # make new dictionary each pass through

        else:                               # "birthday" is in odd index space
            bday_dict["birthday"] = item
            bday_list.append(bday_dict)     # add to list

    bday_json = {}
    bday_json["presidents"] = bday_list
    with open("info.json", "w") as file:
        json.dump(bday_json, file)
    file.close()


if __name__ == '__main__':
    main()