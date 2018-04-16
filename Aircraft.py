
class AircraftList:

    __aircraft_dict = {}
    mile = 1.60934

    def __init__(self, csv):

        self.popAircraftData(csv)

    def popAircraftData(self, csv):

        f = open(csv)

        count = 0

        for line in f:

            if count > 0:
                line = line.split(",")

                if line[2] == "metric":

                    self.__aircraft_dict[line[0]] = float(line[4])

                else:

                    self.__aircraft_dict[line[0]] = float(line[4]) * self.mile
            else:
                count += 1

    def getAircraftData(self):

        return self.__aircraft_dict

    def getRange(self, code):

        return self.__aircraft_dict[code]

    def createNewAircraft(self, code):

        if code in self.__aircraft_dict:

            a_range = self.__aircraft_dict[code]
            return Aircraft(code, a_range)

        else:

            print("Sorry we could not find that aircraft in our database")
            return False


class Aircraft:

    __code = 0

    def __init__(self, code, a_range):

        self.__code = code
        self.__range = a_range

    def getCode(self):

        return self.__code

    def getRange(self):

        return self.__range


