from AirportAtlas import AirportAtlas
from Airplane import Airplane
from fx import ExchangeRate

def main():

    atlas = AirportAtlas("/home/hugh/20230/project/data/airport.csv")

    distance = atlas.getDistance("ORK", "GWY")

    print(distance)

    print(atlas.atlas["ORK"])

    print(atlas.atlas['GWY'].country)

    for i in atlas.atlas:
        if atlas.atlas[i].country == "Ireland":
            print(atlas.atlas[i].code)

    newER = ExchangeRate("/home/hugh/20230/project/data/countrycurrency.csv",
                             "/home/hugh/20230/project/data/currencyrates.csv")

    newAirplane = Airplane("12345")

    cost = atlas.getPrice(newER, 'ORK', 'GWY', newAirplane)

    print("cost of flight =",cost)


main()