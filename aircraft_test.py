from Aircraft import *

new_aircraftList = AircraftList("/home/hugh/20230/project/data/aircraft.csv")

code = input("Please enter code of airplane now")

new_aircraft = new_aircraftList.createNewAircraft(code)

print(new_aircraft.getCode())
print(new_aircraft.getRange())
