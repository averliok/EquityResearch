'''#!/usr/bin/python

from tkinter import *
import tkinter as tk

window = tk.Tk()

def retrieve_input():
    global q
    quote_input = q.get()
    print(quote_input)

q = Entry(window)
print(q)


def create_window():
    window.title('MOEX security analysis tool')
    tk.Label(window, text="Quote").grid(row=0)
    tk.Label(window, text="Starting date").grid(row=1)
    tk.Label(window, text="End date").grid(row=2)
    e1 = tk.Entry(window)
    e2 = tk.Entry(window)
    e3 = tk.Entry(window)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    tk.Button(window, text='Quit', command=window.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
    myText_Box = tk.Button(window, text='Enter', command=retrieve_input).grid(row=3, column=0, sticky=tk.W, pady=4)
    '''
'''class App(object):
    def __init__(self, window, **kwargs):
        self.window = window
        self.create_text()

    def create_text(self):
        text_box = Text(window, height=2, width=10)
        text_box.pack()
        textBox = tk.Button(window, text='Enter', command=lambda: retrieve_input()).grid(row=3, column=2, sticky=tk.W,
'''

'''
def main():
    create_window()
    window.mainloop()
'''