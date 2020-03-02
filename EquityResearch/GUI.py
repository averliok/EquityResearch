from tkinter import *
from tkinter import messagebox
import get_tickers
import re


tickers = get_tickers.get_moex_tickers()


def get_input():
    t = ticker.get()
    s = s_date.get()
    e = e_date.get()
    return t, s, e


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

Button(root, text='Enter', command=get_input()).grid(row=3, column=1)
Button(root, text='Quit', command=root.quit).grid(row=3, column=0)


t, s, e = get_input()


def check_ticker_validity(t):
    if t in tickers:
        return t
    else:
        messagebox.showinfo('Error', 'Invalid ticker')


def date_validity(s, e):
    if re.match(r'\d{4}-\d{2}-\d{2}', s) and re.match(r'\d{4}-\d{2}-\d{2}', e):
        return s, e
    else:
        messagebox.showinfo('Error', 'Invalid format')


root.mainloop()


if __name__ == '__main__':
    get_input()