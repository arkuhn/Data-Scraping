import tkinter as tk
from tkinter import *
import yellowPages


class Application:
    def __init__(self, root):
        self.createWidgets(root)
        root.title("A Simple Data Scrape")
        root.resizable(width=0, height=0)
        root.geometry('{}x{}'.format(800, 600))

    def createWidgets(self, root):

        #Title Label
        title = Label(root, text="Simple Scrape", font=("Helvetica", 24))
        title.pack()
        title.place(relx=0.5, rely=0.3, anchor=CENTER)

        #Interest Label
        interestL = Label(root, text="What are you interested in?")
        interestL.pack()
        interestL.place(relx=0.5, rely=0.7, anchor=CENTER)

        interest = StringVar()
        interest.set("Enter your interest here.")
        zip = StringVar()
        zip.set("Enter your zip here.")

        #Interest input
        interestI = Entry(root, width=50, textvariable=interest)
        interestI.pack()
        interestI.place(relx=0.5, rely=0.8, anchor=CENTER)


        #Zipcode label
        zipL = Label(root, text="What is your zipcode?")
        zipL.pack()
        zipL.place(relx=0.5, rely=0.5, anchor=CENTER)

        #Zipcode input
        zipI = Entry(root, width=50, textvariable=zip)
        zipI.pack()
        zipI.place(relx=0.5, rely=0.6, anchor=CENTER)


        #Run button
        run = tk.Button( text = 'Run', command = lambda: yellowPages.dataget(interest.get(), zip.get()))
        run.pack()
        run.place(relx=.5, rely = .9, anchor=CENTER)


def main():
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

