import random
import requests
from bs4 import BeautifulSoup

# URL = 'http://www.imdb.com/chart/top'


def main():
    # response = requests.get(URL)

    # soup = BeautifulSoup(response.text, 'html.parser')

    # movieTags = soup.select('td.titleColumn')
    # innerMovieTags = soup.select('td.titleColumn a')
    # ratingTags = soup.select('td.posterColumn span[name=ir]')

    # def getYear(movieTags):
    #     movieSplit = movieTags.text.split()
    #     year = movieSplit[-1]
    #     return year

    print("Chegou no main")
    parca = input("Qual seu nome parca ?")

    print("bem vindo, "+parca)


main()
