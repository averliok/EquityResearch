#!/usr/bin/env python3

import time
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import GUI


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


def get_th_info(ticker_list, risk_list, returns_list, variances_list, ticker, class_instance):
    ticker_list.append(ticker)
    risk_list.append(class_instance.get_risk())
    returns_list.append(class_instance.get_ror())
    variances_list.append(class_instance.get_variance())


quotes = []
risk = []
ret = []
variance_list = []


def main():
    ticker, s_date, e_date = GUI.main()
    quote_inf = SecurityInfo(ticker, s_date, e_date)
    get_th_info(quotes, risk, ret, variance_list, ticker, quote_inf)
    dictionary = {'Ticker': quotes, 'Risk': risk, 'Return': ret}
    if GUI.ask_quit():
        main()
    dataframe = pd.DataFrame(dictionary)
    dataframe.set_index('Ticker', inplace=True, drop=True)
    return dataframe


if __name__ == '__main__':
    main()
