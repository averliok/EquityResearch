#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import requests


def get_moex_tickers():
    response = requests.get(
        'http://iss.moex.com//iss/statistics/engines/stock/markets/index/analytics/IMOEX/tickers.xml')
    with open('moex_tickers.xml', 'wb') as file:
        file.write(response.content)
    tree = ET.parse('moex_tickers.xml')
    moex_tickers = [i.attrib['ticker'] for i in tree.iter('row')]
    return moex_tickers


if __name__ == '__main__':
    get_moex_tickers()