"""
Create a dictionary (in your file) of names and birthdays.
When you run your program it should ask the user to enter a name,
and return the birthday of that person back to them.
"""


from bs4 import BeautifulSoup
from datetime import datetime
import requests

def get_bday(dict):
    done = False
    while not done:
        name = input("Enter a President's full name (eg Thomas Jefferson): ")
        try:
            print("{}'s birthday is {}.".format(name, dict[name]))
            done = True
        except KeyError:
            print("I couldn't find {}. Here is a list of Presidents: ".format(name))
            for key in dict.keys():
                print(key)


def gen_bday_dict(list):
    """
    Creates a dictionary of Presidents birthdays where key = name, value = bday
    :param list: expects [key1, value1, key2, value2,...,key_n, value_n] format
    :return: dictionary that has paired all the key/values in list
    """
    bday_dict ={}
    for index, item in enumerate(list):
        if index % 2 == 0:
            key = item
            bday_dict[key] = ""
        else:
            value = item
            bday_dict[key] = value
    return bday_dict


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


def main():   # Runs get_bday with a dictionary of President birthdays
    birthdays = "http://www.indepthinfo.com/articles/presidential-birthdays.shtml"
    bday_list = get_bday_list(birthdays)
    bday_dict = gen_bday_dict(bday_list)
    get_bday(bday_dict)


if __name__ == '__main__':
    main()