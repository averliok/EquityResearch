#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
import get_tickers


ticker_variable = None
s_date_variable = None
e_date_variable = None


class MainWindow:

    def __init__(self, root):
        self.root = root
        self.root.title('MOEX Secuirty Analysis Tool')

        self.ticker = StringVar()
        self.s_date = StringVar()
        self.e_date = StringVar()

        self.L1 = Label(self.root, text='Start date: ')
        self.L1.grid(row=0, column=0, padx=5, pady=5)
        self.L2 = Label(self.root, text='End date: ')
        self.L2.grid(row=1, column=0, padx=5, pady=5)
        self.L3 = Label(self.root, text='Ticker: ')
        self.L3.grid(row=2, column=0, padx=5, pady=5)

        self.E1 = Entry(self.root, textvariable=self.s_date)
        self.E1.grid(row=0, column=1)
        self.E2 = Entry(self.root, textvariable=self.e_date)
        self.E2.grid(row=1, column=1)
        self.E3 = Entry(self.root, textvariable=self.ticker)
        self.E3.grid(row=2, column=1)

        self.B1 = Button(self.root, text='Enter', command=lambda: [self.get_input(),
                                                                   root.quit()])
        self.B1.grid(row=3, column=2)
        self.B2 = Button(self.root, text='Quit', command=root.destroy)
        self.B2.grid(row=3, column=0)
        self.B3 = Button(self.root, text='Clear', command=self.clear_text)
        self.B3.grid(row=3, column=1)

    def get_input(self):
        global ticker_variable
        global s_date_variable
        global e_date_variable

        ticker_variable = self.ticker.get()
        s_date_variable = self.s_date.get()
        e_date_variable = self.e_date.get()

    def clear_text(self):
        self.E1.delete(0, 'end')
        self.E2.delete(0, 'end')
        self.E3.delete(0, 'end')

    def message_pop_up(self):
        messagebox.showinfo('Error', 'Invalid format')
        self.quit()

    def quit(self):
        self.root.destroy()


def is_ticker_valid():
    """
    Check if the input ticker is publicly trade. If it is not, prompt user to input the valid ticker
    """
    tickers = get_tickers.get_moex_tickers()
    if ticker_variable is None:
        return 'None'
    if ticker_variable.upper() in tickers:
        return True
    else:
        return False


def is_date_valid():
    """
    Check the format validity of given timeframe. Should the user input illegal format, they will be prompted
    to re-enter the dates.
    """
    if s_date_variable is None and e_date_variable is None:
        return 'None'
    elif re.match(r"\d{4}-\d{2}-\d{2}", s_date_variable) and \
            re.match(r"\d{4}-\d{2}-\d{2}", e_date_variable):
        return True
    else:
        return False


def fetch_info():
    """
    Assemble all input information into single function
    """
    if ticker_variable is None and s_date_variable is None and e_date_variable is None:
        return 'None'
    elif is_date_valid() and is_ticker_valid():
        return True
    else:
        return False


count = 0


def main():
    global count

    master = Tk()
    WindowClassInstance = MainWindow(master)
    print(count)
    if count > 0:
        master.withdraw()
    master.mainloop()
    if fetch_info() == 'None':
        master.destroy()
    elif fetch_info():
        count += 1
        return ticker_variable, s_date_variable, e_date_variable
    else:
        WindowClassInstance.message_pop_up()
        main()


def ask_quit():
    result = messagebox.askyesno("", "Do you want to continue?")
    return result