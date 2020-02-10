#!/usr/bin/env python3

import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import time
import GetTickers
import pickle
import GUI

tickers = GetTickers.get_moex_tickers()


def df_creation():
    quotes1 = []
    risk1 = []
    ret1 = []
    return quotes1, risk1, ret1


def get_ticker(tickers):
    while True:
        try:
            ticker_input = input('Enter the ticker: ').upper()
        except ValueError:
            raise ValueError('Invalid ticker')
        else:
            if ticker_input in tickers:
                return str(ticker_input)
                break
            else:
                print('Invalid ticker')


def get_dates():
    s_date1 = input('Enter a starting date (format yyyy-mm-dd): ')
    e_date1 = input('Enter an end date (format yyyy-mm-dd): ')
    return s_date1, e_date1


tick = get_ticker(tickers)
s_date, e_date = get_dates()
quotes, risk, ret = df_creation()


class SecurityInfo:
    """
    Get all the relevant information on a single stock within a given time period
    """

    def __init__(self, ticker='', start_date='', end_date=''):
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
    quote_inf = SecurityInfo(tick, s_date, e_date)
    return quote_inf


z = getsecinfo(tick, s_date, e_date)


def get_th_info(z):
    quotes.append(tick)
    risk.append(z.get_risk())
    ret.append(z.get_ror())


if __name__ == '__main__':
    while True:
        get_th_info(z)
        print(quotes)
        print(risk)
        print(ret)
        x = input('Do you want to quit program? [Y/N] ')
        if x.upper() == 'Y':
            break
        else:
            tick = get_ticker(tickers)
            s_date, e_date = get_dates()
            z = getsecinfo(tick, s_date, e_date)
