#!/usr/bin/env python3

import get_security_info
import get_tickers
import plotting

if __name__ == '__main__':
    get_tickers.get_moex_tickers()
    dataframe = get_security_info.main()
    plot = plotting.Plots(dataframe)
    plot.bar_chart()
