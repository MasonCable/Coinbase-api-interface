from MarketData import MarketData

# Thos class is a list of all functions
class Helpers(MarketData):
    def __init__(self):
        pass

    def tester(self):
        d = self.currencies()

        print(d)


Helpers().tester()