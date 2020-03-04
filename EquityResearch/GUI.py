#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox


ticker_variable = ''
s_date_variable = ''
e_date_variable = ''


class MainWindow:

    def __init__(self, root):
        self.root = root
        self.root.title('MOEX Secuirty Analysis Tool')

        self.ticker = StringVar()
        self.s_date = StringVar()
        self.e_date = StringVar()

        self.L1 = Label(self.root, text='Start date: ').grid(row=0, column=0, padx=5, pady=5)
        self.L2 = Label(self.root, text='End date: ').grid(row=1, column=0, padx=5, pady=5)
        self.L3 = Label(self.root, text='Ticker: ').grid(row=2, column=0, padx=5, pady=5)

        self.E1 = Entry(self.root, textvariable=self.s_date).grid(row=0, column=1)
        self.E2 = Entry(self.root, textvariable=self.e_date).grid(row=1, column=1)
        self.E3 = Entry(self.root, textvariable=self.ticker).grid(row=2, column=1)

        self.B1 = Button(self.root, text='Enter', command=lambda: [self.get_input(),
                                                    root.destroy()]).grid(row=3, column=2,
                                                                          padx=5, pady=5)
        self.B2 = Button(self.root, text='Quit', command=lambda: root.destroy()).grid(row=3, column=0, padx=5, pady=5)
        self.get_input()

    def get_input(self):
        global ticker_variable
        global s_date_variable
        global e_date_variable

        ticker_variable = self.ticker.get()
        s_date_variable = self.s_date.get()
        e_date_variable = self.e_date.get()

    def check_ticker_validity(self):
        """
        Check if the input ticker is publicly trade. If it is not, prompt user to input the valid ticker
        """
        self.get_input()
        import get_tickers
        tickers = get_tickers.get_moex_tickers()
        if ticker_variable.upper() in tickers:
            return True
        else:
            return False

    def date_validity(self):
        """
        Check the format validity of given timeframe. Should the user input illegal format, they will be prompted
        to re-enter the dates.
        """
        self.get_input()
        if re.match(r"\d{4}-\d{2}-\d{2}", s_date_variable) and \
                re.match(r"\d{4}-\d{2}-\d{2}", e_date_variable):
            return True
        else:
            return False

    def fetch_info(self):
        """
        Assemble all input information into single function
        """
        if self.date_validity() is True and \
                self.check_ticker_validity() is True:
            return True
        else:
            messagebox.showinfo('Error', 'Invalid format')


def main():
    master = Tk()
    foo = MainWindow(master)
    master.mainloop()
    if foo.fetch_info() is True:
        return ticker_variable, s_date_variable, e_date_variable
    else:
        foo.reset()


def ask_quit():
    result = messagebox.askquestion("", "Do you want to continue?")
    return result
