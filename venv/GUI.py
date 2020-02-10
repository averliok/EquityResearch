#!/usr/bin/python

from tkinter import *
import tkinter as tk


def create():
    window = tk.Tk()
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
    tk.Button(window, text='Clear', command=clear).grid(row=3, column=1, sticky=tk.W, pady=4)
    tk.Button(window, text='Enter', command=lambda: retrieve_input).grid(row=3, column=2, sticky=tk.W, pady=4)
    window.mainloop()

def retrieve_input():
    inputValue = textBox.get("1.0", "end-1c")


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)