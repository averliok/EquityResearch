#!/usr/bin/env python3

import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import time
import GetTickers
import re

tickers = GetTickers.get_moex_tickers()


def get_ticker(tickers):
    while True:
        try:
            ticker_input = input('Enter the ticker: ')
        except ValueError:
            raise ValueError('Invalid ticker')
        else:
            if ticker_input in tickers:
                return str(ticker_input)
                break
            else:
                print('Invalid ticker')


def get_dates():
    pattern = re.compile('r([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))')
    while True:
        try:
            s_date = input('Enter a starting date (format yyyy-mm-dd): ')
            e_date = input('Enter an end date (format yyyy-mm-dd): ')
        except ValueError:
            raise ValueError('Incorrect data format, should be YYYY-MM-DD')
        return s_date, e_date

if __name__ == '__main__':
    tick = get_ticker(tickers)
    s_date, e_date = get_dates()


class SecurityInfo:
    """
    Get all the relevant information on a single stock within a given time period
    """

    def __init__(self, ticker=tick, start_date=s_date, end_date=e_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.log_return = None
        self.delta = int
        self._calculate_date_duration()
        self.get_log_return()

    def _calculate_date_duration(self):
        start_date = self.start_date
        end_date = self.end_date
        start_date = time.strptime(start_date, '%Y-%m-%d')
        end_date = time.strptime(end_date, '%Y-%m-%d')
        # Convert string date to datetime object
        d0 = time.mktime(start_date)
        d1 = time.mktime(end_date)
        # Convert datetime object to seconds
        delta = d1 - d0
        self.delta = round(delta / 120960)
        # Get seconds to hours (/3600), to days (/24), divide by weeks(/7) and multiply by workdays(*5)
        return self.delta

    def get_log_return(self):
        quote = self.ticker
        start_date = self.start_date
        end_date = self.end_date
        quote = wb.DataReader(quote, data_source='moex', start=start_date, end=end_date)
        # Fetch information about stock from Moscow Stock Exchange
        quote['log return'] = np.log(quote['CLOSE'] / quote['CLOSE'].shift(1))
        # Get the logarithmic return of each day individually
        self.log_return = quote['log return']
        # Calculate logarithmic return
        return quote['log return']

    def get_ror(self):
        quote = self.log_return.mean() * self.delta
        rate_of_return = round(quote, 5) * 100
        # Get security's rate of return
        return rate_of_return

    def get_risk(self):
        risk = self.log_return
        risk = (risk.std() * self.delta) ** 0.5
        # Get the standard deviation of an individual stock
        return round(risk, 5)


def getsecinfo(tick, s_date, e_date):
    quote = SecurityInfo(tick, s_date, e_date)
    quotes = []
    risk = []
    ret = []
    quotes.append(tick)
    risk.append(quote.get_risk())
    ret.append(quote.get_ror())
    print(quotes)
    print(risk)
    print(ret)


getsecinfo(tick, s_date, e_date)
