class ExchangeRate:

    _exchangeRates = {}
    _currencyInfo = {}

    def __init__(self, currency_info, er_info):

        #constructor creates database for both currency names and for currency rates
        #currency info holds, currency name and currency codes
        #currency rates holds currency codes and currency exchange rates
        self.getCurrencyInfo(currency_info)
        self.getERInfo(er_info)

    def getCurrencyInfo(self, currency_info):

        fc = open(currency_info)

        for line in fc:
            line = line.split(",")
            self._currencyInfo[line[0]] = line[-6]

    def getERInfo(self, ERinfo):

        fe = open(ERinfo)

        for line in fe:
            line = line.split(",")
            self._exchangeRates[line[1]] = line[2]










