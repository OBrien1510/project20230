from Airport import Airport
import math

class AirportAtlas():

    _atlas = {}

    def __init__(self, data):

        self.getData(data)

    def getData(self, data):
        f = open(data)

        for line in f:
            line = line.split(",")
            # code, lat, long, country, name
            if line[1] != "All Airports":
                x = Airport(line[4], line[6], line[7], line[3], line[1])
                self._atlas[line[4]] = x


    def getAirport(self, code):

        return self._atlas[code]

    @staticmethod
    def greatCircledList(long1, long2, lat1, lat2):

        radius_earth = 6731
        theta1 = float(long1) * (2 * math.pi) / 360
        theta2 = float(long2) * (2 * math.pi) / 360
        phi1 = (90 - float(lat1)) * (2 * math.pi) / 360
        phi2 = (90 - float(lat2)) * (2 * math.pi) / 360
        distance = math.acos(math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) + math.cos(phi1) * math.cos(phi2)) * radius_earth

        return distance

    def getDistance(self, code1, code2):

        a1 = self.getAirport(code1)
        a2 = self.getAirport(code2)

        distance = self.greatCircledList(a1.long, a2.long, a1.lat, a2.lat)

        return distance

    def getPrice(self, er, code1, code2, airplane):

        """

        :param er: Exchange rate class instance
        :param code1: airport code 1
        :param code2: airport code 2
        :return: cost of the flight between the 2 in the local currency of the first country

        1. get the distance between 2 codes
        2. convert codes to country
        3. convert country to currency code
        4. convert currency code to ER
        5. multiply required fuel by the exchange rate
        """

        distance = self.getDistance(code1, code2)

        airport1 = self._atlas[code1]


        country1 = airport1.country


        print(country1)

        country1Currency = er._currencyInfo[country1]

        print(country1Currency)

        country1ER = er._exchangeRates[country1Currency]




        airplane.check(distance)

        return distance * float(country1ER)









