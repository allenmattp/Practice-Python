"""
instead of printing the results to a screen, write the results to a txt file.
This file pulls market data from the first page of Yahoo Finance charts
"""

from bs4 import BeautifulSoup
from datetime import datetime
import requests

# Various Yahoo Finance charts
trending = "https://finance.yahoo.com/trending-tickers"
active = "https://finance.yahoo.com/most-active"
gainers = "https://finance.yahoo.com/gainers"
losers = "https://finance.yahoo.com/losers"
crypto = "https://finance.yahoo.com/cryptocurrencies"

def main(url):
    # Use requests to get a website
    r = requests.get(url)
    # Use beautiful soup to convert response into text using html parser
    soup = BeautifulSoup(r.text, "html.parser")
    # find all columns in crypto table
    cols = soup.find_all("td")
    # Open file to write to
    with open("exercise_21_file.txt", "w") as file:
        # Write timestamp at top of document for when request is made
        file.write(datetime.now().isoformat(timespec="seconds") + "\n")
        # Write an error message if nothing is returned
        if not len(cols):
            print("Whoops, we couldn't find anything.")
            file.write("EMPTY")
        # Write all columns to file
        else:
            for col in cols:
                # pull the column's attributes so we can write its label
                attr = col.attrs
                file.write("\n" + attr["aria-label"] + ": ")
                file.write(col.text.strip())
    file.close()


if __name__ == '__main__':
    main(crypto)