#!/usr/bin/env python3

import GetSecurityInfo
import GetTickers
import plotting


if __name__ == '__main__':
    GetTickers.get_moex_tickers()
    dataframe = GetSecurityInfo.main()
    print(dataframe)
    plotting.bar_plot(dataframe)