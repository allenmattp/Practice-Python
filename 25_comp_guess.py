"""
You, the user, will have in your head a number between 0 and 100.
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
At the end of this exchange, your program should print out how many guesses it took to get your number.
"""
import time


def start():
    print("I will guess your number!")
    number = int(input("How high can my number be? "))
    print("OK, think of a number between 1 and", number, "...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(". .")
    time.sleep(1)
    print(". . .")
    time.sleep(1)
    ready = str(input("Are you ready? ")).lower()
    if "y" in ready:
        main(number)
    else:
        print("OK. I'll give you more time.")
        time.sleep(5)
        start()

def main(n):
    count = 0
    guess_cache = [x for x in range(1, n)]
    correct = False

    while not correct:
        mid_pos = len(guess_cache) // 2
        count += 1
        try:
            print("Your number is", guess_cache[mid_pos])
            reply = str(input("Am I correct? Or is it higher/lower?")).lower()

            if "y" in reply:
                print("I am a genius!")
                print("It only took", count, "guesses.")
                correct = True
            elif "h" in reply:
                print("Hmm... It's higher than that?")
                guess_cache = guess_cache[mid_pos:]
            elif "l" in reply:
                print("Hmm... It's lower than that?")
                guess_cache = guess_cache[:mid_pos]
            else:
                print("You're just stalling for time now.")
                count -= 1
        except IndexError:
            print("LIAR!!!")

if __name__ == '__main__':
    start()