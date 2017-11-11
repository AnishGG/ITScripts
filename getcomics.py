from bs4 import BeautifulSoup
import requests
import sys
import time
import urllib.request

def make_soup(url):
    req = requests.get(url)
    html = req.content
    return BeautifulSoup(html, 'html.parser')

def get_images(n, path):
    url1 = 'https://xkcd.com/'
    url2 = ""
    lis = []
    strin = ""
    n = int(n)
    for i in range(n):
        url2 =  url1 + strin
        soup = make_soup(url2)
        strin = soup.find("ul", class_="comicNav").find(rel='prev')['href']
#        print(strin)
        url = soup.find('div', id='comic').find('img')['src']
        actualUrl = "http:" + url
        lis = actualUrl.split("/")
        filename = lis[len(lis) - 1]
        filename = path + '/' + filename
#        print(filename, actualUrl)
        try:
            print("Downloading image to ", path)
            urllib.request.urlretrieve(actualUrl, filename)
            print("Success...")
        except:
            print("An error occured while fetching file. Continuing..")


if __name__ == '__main__':
    n = sys.argv[1]
    path = sys.argv[2]
    get_images(n, path)
