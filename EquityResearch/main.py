#!/usr/bin/env python3

import get_security_info
import get_tickers
import plotting
import GUI


if __name__ == '__main__':
    get_tickers.get_moex_tickers()
    dataframe, variances = get_security_info.main()
    print(dataframe)
    print(variances)
    x = variances.corr()
    print(x)
    #print(returns.cov())
    plot = plotting.Plots(dataframe)
    plot.bar_chart()
    GUI.get_input()
