
__author__ = 'Adam'

import requests
from bs4 import BeautifulSoup

def dataget(interest, zipcode):
    r = requests.get("http://www.yellowpages.com/search?search_terms="+interest+"&geo_location_terms="+zipcode+"")
    soup = BeautifulSoup(r.content, "html.parser")
    g_data = soup.find_all("div", {"class":"info"})
    for item in g_data:
        try:
            print(item.contents[0].find_all("a", {"class":"business-name"})[0].text)
        except:
            pass
        try:
            print(item.contents[1].find_all("span", {"itemprop":"streetAddress"})[0].text)
            print(item.contents[1].find_all("span", {"itemprop":"addressLocality"})[0].text, item.contents[1].find_all("span", {"itemprop":"postalCode"})[0].text)
        except:
            pass
        try:
            print(item.contents[1].find_all("li", {"class":"phone primary"})[0].text)
        except:
            pass
        print("-----------------")

def dict(word):
    r = requests.get("http://www.merriam-webster.com/dictionary/"+word+"")
    soup = BeautifulSoup(r.content)
    g_data2 = soup.find_all("div", {"class":"scnt"})
    for item in g_data2:
        try:
            print(item.contents[0].find_all("div", {"class":"scnt"}))
        except:
            pass

