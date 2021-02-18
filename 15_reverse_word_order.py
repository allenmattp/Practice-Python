"""
Write a program that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
"""

def main():
    def reverse():
        # split string on whitespace into string_list, starting from last word
        string_list = str(input("Enter text: ")).split()[::-1]
        # join our string_list with words separated by a space and return
        return " ".join(string_list)

    print(reverse())

if __name__ == '__main__':
    main()