from fx import ExchangeRate
from AirportAtlas import AirportAtlas
from Airplane import Airplane
import sys
from Aircraft import *

def repeat():

    repeat = 0

    while repeat != 1 or repeat != 2:
        repeat = int(input("Press 1 to return to the menu or 2 to exit\n"))

        if repeat == 2:
            exit()

        elif repeat != 1:
            print("Invalid option, please try again")

        else:
            return True



def main(airport, er, currency, aircraft):

    newEr = ExchangeRate(currency, er)

    newAtlas = AirportAtlas(airport)

    newAirplaneList = Aircraft(aircraft)

    newAirplane = Airplane("12345")

    user_input = 0

    country_search = 0

    while user_input != 6:

        print("Please select and option: ")
        print("[1] Get list of airports in a particular country")
        print("[2] Get the aiport code of a specific airport")
        print("[3] Get distance between 2 aiports (using their relevant aiport codes")
        print("[4] Get fuel cost of a journey between 2 aiports")
        print("[5] Get fuel price for a specific route")
        print("[6] Exit")
        print()
        user_input = int(input(" 1, 2, 3, 4 or 5\n"))

        if user_input == 1:
            country = input("Please enter the country for which you want a list of airports\n")
            country_search = input("If you would like to restrict search results to aiports starting with a specific letter, please enter letter now or press enter to skip this option")
            found_country = False
            found_letter = False
            if country_search != "":
                for i in newAtlas._atlas:
                    if newAtlas._atlas[i].country == country:
                        found_country = True
                        if newAtlas._atlas[i].name[0] == country_search.upper():
                            found_letter = True
                            print(newAtlas._atlas[i].name)
                if not found_country:
                    found_letter = True
                    print("Sorry we could not find a record of the country you entered\n")
                if not found_letter:
                    print("No airport could be found beginning withe letter '%s'" % country_search.upper())

                again = repeat()

                if again:
                    user_input = 0

                else:
                    user_input = 5
            else:
                for i in newAtlas._atlas:
                    if newAtlas._atlas[i].country == country:
                        found = True
                        print(newAtlas._atlas[i].name)
                if not found:
                    print("Sorry we could not find a record of the country you entered\n")

                again = repeat()

                if again:
                    user_input = 0

                else:
                    user_input = 5



        elif user_input == 2:
            name = input("Please enter the airport for which you want a code\n")
            print()
            found = False
            for i in newAtlas._atlas:

                if newAtlas._atlas[i].name == name:
                    print(newAtlas._atlas[i].code)
                    found = True

            if not found:
                print("We're sorry but we could not find an airport with the name",name,"in our database")
                print()
                print("Please try and use the services provided to find the exact name of the airport in our database if you wish")

            again = repeat()

            if again:
                user_input = 0

            else:
                user_input = 5



        elif user_input == 3:
            code1 = input("Please enter airport code of the original airport\n")
            code2 = input("Please enter airport code of destination airport\n")

            found1 = False
            found2 = False

            for i in newAtlas._atlas:
                if newAtlas._atlas[i].code == code1:
                    found1 = True
                elif newAtlas._atlas[i].code == code2:
                    found2 = True


            if found1 and found2:

                distance = newAtlas.getDistance(code1, code2)

                print("Distance between 2 airports:",distance,"km")

            elif not found1 and found2:

                print("Sorry but we could not find",code1,"in our records")

            elif not found2 and found1:

                print("Sorry but we could not find",code2,"in our records")

            else:

                print("Sorry we could not find either",code1,"or",code2,"in our records")

            again = repeat()

            if again:
                user_input = 0

            else:
                user_input = 5


        elif user_input == 4:

            code1 = input("Please enter the airport code of the first airport\n")
            code2 = input("Please enter the airport code of the destination aiport\n")
            airplane = input("Please enter the code of the aircraft for the journey")

            newAircraft = AircraftList.createNewAircraft(airplane)

            if not newAircraft:
                again = repeat()

            else:



                found1 = False
                found2 = False

                for i in newAtlas._atlas:
                    if newAtlas._atlas[i].code == code1:
                        found1 = True
                    elif newAtlas._atlas[i].code == code2:
                        found2 = True

                if found1 and found2:

                    distance = newAtlas.getDistance(code1, code2)

                    a_range = newAircraft.getRange()

                    if a_range >= distance:

                        cost = newAtlas.getPrice(newEr, code1,code2, newAirplane)

                        for i in newAtlas._atlas:
                            if newAtlas._atlas[i].code == code1:
                                country = newAtlas._atlas[i].country


                        print("Fuel cost between 2 airports:", cost, "EUR")

                    else:

                        print("Aircraft selected does not have the range for this journey")

                elif not found1 and found2:

                    print("Sorry but we could not find", code1, "in our records")

                elif not found2 and found1:

                    print("Sorry but we could not find", code2, "in our records")

                else:

                    print("Sorry we could not find either", code1, "or", code2, "in our records")

                again = repeat()

            if again:
                user_input = 0

            else:
                user_input = 5


        elif user_input == 5:
            airport_list = []
            count = 1
            airport = "first"
            while airport != "":
                airport = input("Please enter airport code #" + str(count) + " or hit enter to submit")
                if airport != "":
                    airport_list.append(airport)

            print(airport_list)

            i = 0
            total = 0

            while i < len(airport_list) - 1:

                found1 = False
                found2 = False

                for j in newAtlas._atlas:
                    if newAtlas._atlas[j].code == airport_list[i]:
                        found1 = True
                    elif newAtlas._atlas[j].code == airport_list[i + 1]:
                        found2 = True

                if found1 and found2:

                    cost = newAtlas.getPrice(newEr, airport_list[i], airport_list[i + 1], newAirplane)
                    total += cost

                elif not found1:

                    print("Sorry we could not find a airport with the code",airport_list[i],"in our database")
                    break
                else:

                    print("Sorry we could not find a airport with the code", airport_list[i + 1], "in our database")
                    break

                i += 1

            if found1 and found2:

                for i in newAtlas._atlas:
                    if newAtlas._atlas[i].code == airport_list[0]:
                        country = newAtlas._atlas[i].country

                currency = newEr._currencyInfo[country]

                print("total cost:",total,currency)

            again = repeat()

            if again:
                user_input = 0

            else:
                user_input = 5


        elif user_input == 6:
            exit()

        else:
            print("Sorry that was not a valid option, would you like to try again?")
            user_input = input("y/n?\n")

            if user_input == "n":
                user_input = 6



#main("/home/hugh/20230/project/data/airport.csv", "/home/hugh/20230/project/data/currencyrates.csv", "/home/hugh/20230/project/data/countrycurrency.csv", /home/hugh/20230/project/data/aircraft.csv)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
