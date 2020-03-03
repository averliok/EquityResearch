#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox

import get_tickers


def get_input(ticker_input, s_date_input, e_date_input):
    """
    Supplementary function to ge user input and pass it to the Security Analysis class
    """
    ticker = ticker_input.get()
    s_date = s_date_input.get()
    e_date = e_date_input.get()
    return ticker, s_date, e_date


def main():
    """
    Main function to create TKinter GUI for I/O
    """
    root = Tk()
    root.title('MOEX Security Analysis tool')

    ticker = StringVar()
    s_date = StringVar()
    e_date = StringVar()

    s_date_field = Label(text='Start date: ')
    s_date_field.grid(row=0, column=0)
    e_date_field = Label(text='End date: ')
    e_date_field.grid(row=1, column=0)
    ticker_field = Label(text='Ticker: ')
    ticker_field.grid(row=2, column=0)

    ticker_entry = Entry(textvariable=ticker)
    ticker_entry.grid(row=0, column=1)
    s_date_entry = Entry(textvariable=s_date)
    s_date_entry.grid(row=1, column=1)
    e_date_entry = Entry(textvariable=e_date)
    e_date_entry.grid(row=2, column=1)

    Button(root, text='Enter', command=lambda: [get_input(ticker, s_date, e_date),
                                                root.destroy()]).grid(row=3, column=2)
    Button(root, text='Quit', command=root.destroy).grid(row=3, column=0)
    root.mainloop()
    return ticker, s_date, e_date


def check_ticker_validity(t):
    """
    Check if the input ticker is publicly trade. If it is not, prompt user to input the valid ticker
    """
    tickers = get_tickers.get_moex_tickers()
    if t in tickers:
        return t
    else:
        messagebox.showinfo('Error', 'Invalid ticker')
        main()


def date_validity(s_date, e_date):
    """
    Check the format validity of given timeframe. Should the user input illegal format, they will be prompted
    to re-enter the dates.
    """
    if re.match(r'\d{4}-\d{2}-\d{2}', s_date) and re.match(r'\d{4}-\d{2}-\d{2}', e_date):
        return s_date, e_date
    else:
        messagebox.showinfo('Error', 'Invalid format')
        main()


def get_cont_input(user_input):
    """
    Supplementary function to help user navigate the program
    """
    string = user_input.get()
    return string


def ask_continue():
    """
    Prompt user to continue his research or exit program
    """
    root = Tk()
    root.title('Prompt')
    user_input = StringVar()
    post = Label(text="Do you want to continue? [Y/N] ")
    post.grid(row=0, column=0)
    entry = Entry(textvariable=user_input)
    entry.grid(row=0, column=1)
    Button(root, text='Enter', command=lambda: [get_cont_input(user_input),
                                                root.destroy()]).grid(row=1, column=1)
    Button(root, text='Quit', command=root.destroy).grid(row=1, column=0)
    root.mainloop()
    return user_input
