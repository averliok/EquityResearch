#!/usr/bin/env python3


class Plots:
    """
    Plot the graphs using prompted tickers. WIP
    """

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def bar_chart(self):
        dataframe = self.dataframe
        bar_plot = dataframe.plot(kind='bar', y=['Return', 'Risk'], use_index=True)
        fig = bar_plot.get_figure()
        fig.savefig('bar_chart.png', bbox_inches='tight')
