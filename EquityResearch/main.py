#!/usr/bin/env python3

import get_security_info
import get_tickers
import plotting
import portfolio
import de


if __name__ == '__main__':
    get_tickers.get_moex_tickers()
    dataframe, variances = get_security_info.main()
    print(dataframe)
    print(variances)
    print(variances.cov())
    #print(returns.cov())
    plot = plotting.plots(dataframe)
    plot.bar_chart()
    de.hello()
