import xml.etree.ElementTree as ET
import requests

def get_moex_tickers():
    response = requests.get(
        'http://iss.moex.com//iss/statistics/engines/stock/markets/index/analytics/IMOEX/tickers.xml')
    with open('moex_tickers.xml', 'wb') as file:
        file.write(response.content)
    moex_tickers = []
    tree = ET.parse('moex_tickers.xml')
    for i in tree.iter('row'):
        ticker = i.attrib['ticker']
        moex_tickers.append(ticker)
    return moex_tickers
