class Airport:

    def __init__(self, code, lat, long, country, name):
        self.code = code
        self.lat = lat
        self.long = long
        self.country = country
        self.name = name

    def __str__(self):

        output = "code:",self.code,"latitude:", self.lat,"longitude:",self.long,"country:",self.country

        return str(output)

