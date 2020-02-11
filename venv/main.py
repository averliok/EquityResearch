#!/usr/bin/env python3

import GetSecurityInfo
import GetTickers
import GUI
import plotting


if __name__ == '__main__':
    GetTickers.get_moex_tickers()
    dataframe = GetSecurityInfo.main()
    plotting.bar_plot(dataframe)