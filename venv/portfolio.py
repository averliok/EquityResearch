#!/usr/bin/env python3


import numpy as np
import GetSecurityInfo


def covariance(returns):
    cov = returns.cov()
    corr = returns.corr()
    return cov

'''def distribution():
    input_weights = [int(x)/100 for x in input('Please, state the percentage of each stock in your portfolio'
                                               'in percents: ').split()]
    weights = np.array(input_weights)
    return weights'''

'''distribution()
'''

if __name__ == '__main__':
    main()