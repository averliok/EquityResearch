#!/usr/bin/env python3

import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import time
import GetTickers
import re

tickers = GetTickers.get_moex_tickers()


def get_ticker(tickers):
    while True:
        try:
            ticker_input = input('Enter the ticker: ').upper()
        except ValueError:
            raise ValueError('Invalid ticker')
        else:
            if ticker_input in tickers:
                return str(ticker_input)
            else:
                print('Invalid ticker')


def get_dates():
    while True:
        s_date1 = input('Enter a starting date (format yyyy-mm-dd): ')
        e_date1 = input('Enter an end date (format yyyy-mm-dd): ')
        if re.match(r'\d{4}-\d{2}-\d{2}', s_date1) and re.match(r'\d{4}-\d{2}-\d{2}', e_date1):
            return s_date1, e_date1
        else:
            print("Invalid format")




class SecurityInfo:
    """
    Get all the relevant information on a single stock within a given time period
    """

    def __init__(self, ticker='', start_date='', end_date=''):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.log_return = None
        self.delta = 0
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

    def get_variance(self):
        ror = self.log_return
        variance = ror.var() * self.delta
        return round(variance, 5)



def getsecinfo(tick, s_date, e_date):
    quote_inf = SecurityInfo(tick, s_date, e_date)
    return quote_inf


def get_th_info(q_list, r_list, re_list, v_list, tick, z):
    q_list.append(tick)
    r_list.append(z.get_risk())
    re_list.append(z.get_ror())
    v_list.append(z.get_variance())

def main():
    quotes = []
    risk = []
    ret = []
    variance_list = []
    s_date, e_date = get_dates()
    tick = get_ticker(tickers)
    quote_inf = SecurityInfo(tick, s_date, e_date)
    while True:
        get_th_info(quotes, risk, ret, variance_list, tick, quote_inf)
        dictionary_a = {'Ticker': quotes, 'Risk': risk, 'Return': ret}
        df1 = pd.DataFrame(dictionary_a)
        df2 = pd.DataFrame(variance_list)
        print(df1)
        print(df2)
        x = input('Do you want to quit program? [Y/N] ')
        if x.upper() == 'Y':
            df1.set_index('Ticker', inplace=True, drop=True)
            return df1, df2
        else:
            tick = get_ticker(tickers)
            quote_inf = getsecinfo(tick, s_date, e_date)

if __name__ == '__main__':
    main()