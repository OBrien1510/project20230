from fx import ExchangeRate

newER = ExchangeRate("/home/hugh/20230/project/data/countrycurrency.csv", "/home/hugh/20230/project/data/currencyrates.csv")

print(newER._currencyInfo["Ireland"])

code = newER._currencyInfo["United States"]

print(newER._exchangeRates[code])

currency = newER._exchangeRates[code]

print(currency)

currency2 = newER._currencyInfo['Ireland']

print(currency2)

