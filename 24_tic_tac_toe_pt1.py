"""
Draw a  game board using pseudo graphics
"""


def get_board_size():
    try:
        size = int(input("Enter board size: "))
        return size
    except ValueError:
        print("Try a valid number.")
        main(get_board_size())
        return False

def main(num):
    hori = " ---"
    vert = "|   "
    # Don't run if invalid num provided
    if num:
        for i in range(num):
            print(hori * num)
            print(vert * (num + 1))
        print(hori * num)


if __name__ == '__main__':
    main(get_board_size())