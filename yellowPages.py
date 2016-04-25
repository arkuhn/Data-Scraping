
__author__ = 'Adam'

import requests
import tkinter as tk
from tkinter import *
from bs4 import BeautifulSoup

root = tk.Tk()


def dataget(food, zipcode):
    r = requests.get("http://www.yellowpages.com/search?search_terms="+food+"&geo_location_terms="+zipcode+"")
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

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        root.title("A Simple Data Scrape")
        root.resizable(width=0, height=0)
        root.geometry('{}x{}'.format(800, 600))

    def createWidgets(self):
        #listb = Listbox(root)
        #listb.pack()

        e = Entry(root, width=50)
        e.pack()

        interest = e.get()
        self.QUIT = tk.Button(self, text="Quit", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

def main():
    #food = input("What are you looking for: ")
    #zipcode = input("What zipcode?: ")
    #dataget(food, zipcode)


    app = Application(master=root)
    app.mainloop()
    #word = input("Define what: ")
    #dict(word)


main()