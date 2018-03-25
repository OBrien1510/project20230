class ExchangeRate:

    _exchangeRates = {}
    _currencyInfo = {}

    def __init__(self, currency_info, er_info):

        self.getCurrencyInfo(currency_info)
        self.getERInfo(er_info)

    def getCurrencyInfo(self, currency_info):

        fc = open(currency_info)

        for line in fc:
            line = line.split(",")
            self._currencyInfo[line[0]] = line[14]

    def getERInfo(self, ERinfo):

        fe = open(ERinfo)

        for line in fe:
            line = line.split(",")
            self._exchangeRates[line[1]] = line[3]










