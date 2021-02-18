"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
"""

from bs4 import BeautifulSoup
import requests

def main():

    def scraper(url):
        # Use requests to get a website
        r = requests.get(url)
        # Use beautiful soup to convert response into text using html parser
        soup = BeautifulSoup(r.text, "html.parser")
        # Go through and return all front page posts
        for heading in soup.find_all("p", class_="title"):
           print(heading.a.text.strip())

    # run function for reddit (other sites will require modifications)
    scraper("http://old.reddit.com/r/nba")

if __name__ == '__main__':
    main()