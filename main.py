# region imports
from AlgorithmImports import *
import pandas as pd
import numpy as np
# endregion

class CryptoStrategy(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2021, 1, 1)
        self.SetEndDate(2024, 1, 1)
        self.SetCash(200)

        self.btc = self.AddCrypto("BTCUSD", Resolution.Daily, Market.GDAX).Symbol
        self.eth = self.AddCrypto("ETHUSD", Resolution.Daily, Market.GDAX).Symbol

        self.assets = [self.btc, self.eth]
        
        self.weights = {
            self.btc: 0.5,
            self.eth: 0.5
        }

        
        self.Schedule.On(self.DateRules.EveryDay(), self.TimeRules.At(0, 0), self.Rebalance)

    def OnData(self, data):
        pass  
    def Rebalance(self):
        for symbol in self.assets:
            if self.Portfolio[symbol].Invested:
                self.Liquidate(symbol)
        
        for symbol in self.assets:
            if self.Securities[symbol].Price > 0:
                self.SetHoldings(symbol, self.weights[symbol])
    
    