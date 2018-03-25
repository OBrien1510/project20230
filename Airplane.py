class Airplane:

    __minFuel = 200

    def __init__(self, number):

        self.flightNumber = number
        self.fuel = 0
        self.clearance = False

    def refuel(self, fuel):
        distance = self.fuel + fuel
        self.fuel += fuel
        self.check(distance)

    def check(self, distance):

        if self.fuel < distance:
            self.refuel(distance - self.fuel)

    def takeOff(self):

        if self.clearance:
            print("Taking off")
            self.clearance = False

