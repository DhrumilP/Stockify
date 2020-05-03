import requests
from bs4 import BeautifulSoup
import pandas as pd


class MostActiveScraper:
    def __init__(self):
        self.stockSymbol=[]
        self.stockNames = []
        self.stockPrices = []
        self.stockChanges = []
        self.stockPercents = []
        self.stockVolumes = []
        self.stockAveVolumes = []
        self.stockMarketCaps = []
        self.financeDataFrame = None

        self.getData()
        self.makeDataFrame()
        self.printFrame()

    def getData(self):
        # Yahoo Finance website
        financeURL = "https://ca.finance.yahoo.com/most-active"
        r = requests.get(financeURL)
        financeData = r.text
        soup = BeautifulSoup(financeData, features="html.parser")

        # get data from finance page
        for entry in soup.find_all('tr', attrs={"class": "simpTblRow"}):
            for stockSymbol in entry.find_all('td', attrs={'aria-label': 'Symbol'}):
                self.stockSymbol.append(stockSymbol.text)
            for stockName in entry.find_all('td', attrs={'aria-label': 'Name'}):
                self.stockNames.append(stockName.text)
            for stockPrice in entry.find_all('td', attrs={'aria-label': 'Price (Intraday)'}):
                self.stockPrices.append(stockPrice.find('span').text)
            for stockChange in entry.find_all('td', attrs={'aria-label': 'Change'}):
                self.stockChanges.append(stockChange.text)
            for stockPercent in entry.find_all('td', attrs={'aria-label': '% Change'}):
                self.stockPercents.append(stockPercent.text)
            for stockMarketCap in entry.find_all('td', attrs={'aria-label': 'Market Cap'}):
                self.stockMarketCaps.append(stockMarketCap.text)
            for stockAveVolume in entry.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'}):
                self.stockAveVolumes.append(stockAveVolume.text)
            for stockVolume in entry.find_all('td', attrs={'aria-label': 'Volume'}):
                self.stockVolumes.append(stockVolume.text)

    def makeDataFrame(self):
        # correlate column titles to rows
        for count in range(0,len(self.stockPrices)):
            self.stockPrices[count] = str(self.stockPrices[count].replace(',','.'))
            self.stockChanges[count] = str(self.stockChanges[count].replace(',','.'))
            self.stockPercents[count] = str(self.stockPercents[count].replace(',','.'))
            self.stockMarketCaps[count] = str(self.stockMarketCaps[count].replace(',','.'))
            self.stockAveVolumes[count] = str(self.stockAveVolumes[count].replace(',','.'))
            self.stockVolumes[count] = str(self.stockVolumes[count].replace(',','.'))
        a = {
            "Symbol:": self.stockSymbol,
            "Names": self.stockNames,
            "Prices": self.stockPrices,
            "Change": self.stockChanges,
            "% Change": self.stockPercents,
            "Market Cap": self.stockMarketCaps,
            "Avg Volume (3 Months)": self.stockAveVolumes,
            "Volume": self.stockVolumes
        }

        # create data frame
        self.financeDataFrame = pd.DataFrame.from_dict(a, 'index').transpose()

    def printFrame(self):
        # print data frame
        self.financeDataFrame.to_csv(r'trial.csv', index = False)
        # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            # print(self.financeDataFrame.to_string())


def run():
    MostActiveScraper()
