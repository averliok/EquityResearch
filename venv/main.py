#!/usr/bin/env python3

import GetSecurityInfo
import GetTickers
import plotting
import portfolio


if __name__ == '__main__':
    GetTickers.get_moex_tickers()
    dataframe, returns = GetSecurityInfo.main()
    print(dataframe)
    #print(returns.cov())
    plotting.bar_plot(dataframe)
