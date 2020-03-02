#!/usr/bin/env python3


import numpy as np
import get_security_info


def covariance(returns):
    cov = returns.cov()
    corr = returns.corr()
    return cov


if __name__ == '__main__':
    main()