#!/usr/bin/env python3


import matplotlib.pyplot as plt


def plot(dataframe):
    return dataframe.plot(kind='bar', y=['Return', 'Risk'], use_index=True)
