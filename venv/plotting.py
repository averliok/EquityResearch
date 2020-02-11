#!/usr/bin/env python3


import matplotlib.pyplot as plt


def bar_plot(dataframe):
    x = dataframe.plot(kind='bar', y=['Return', 'Risk'], use_index=True)
    x.figure.savefig('bar_chart.png')

