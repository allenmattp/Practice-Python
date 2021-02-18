"""
Write a program that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
"""

def main():
    def reverse():
        string_list = str(input("Enter text: ")).split()[::-1]
        return " ".join(string_list)

    print(reverse())

if __name__ == '__main__':
    main()