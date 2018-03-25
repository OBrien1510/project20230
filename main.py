from fx import ExchangeRate
from AirportAtlas import AirportAtlas
from Airplane import Airplane
import sys

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



def main(airport, er, currency):

    newEr = ExchangeRate(currency, er)

    newAtlas = AirportAtlas(airport)

    newAirplane = Airplane("12345")

    user_input = 0

    while user_input != 5:

        print("Please select and option: ")
        print("[1] Get list of airports in a particular country")
        print("[2] Get the aiport code of a specific airport")
        print("[3] Get distance between 2 aiports (using their relevant aiport codes")
        print("[4] Get fuel cost of a journey between 2 aiports")
        print("[5] Exit")
        print()
        user_input = int(input(" 1, 2, 3, 4 or 5\n"))

        if user_input == 1:
            country = input("Please enter the country for which you want a list of airports\n")
            found = False
            for i in newAtlas.atlas:
                if newAtlas.atlas[i].country == country:
                    found = True
                    print(newAtlas.atlas[i].name)
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
            for i in newAtlas.atlas:

                if newAtlas.atlas[i].name == name:
                    print(newAtlas.atlas[i].code)
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

            for i in newAtlas.atlas:
                if newAtlas.atlas[i].code == code1:
                    found1 = True
                elif newAtlas.atlas[i].code == code2:
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

            found1 = False
            found2 = False

            for i in newAtlas.atlas:
                if newAtlas.atlas[i].code == code1:
                    found1 = True
                elif newAtlas.atlas[i].code == code2:
                    found2 = True

            if found1 and found2:

                cost = newAtlas.getPrice(newEr, code1,code2, newAirplane)

                for i in newAtlas.atlas:
                    if newAtlas.atlas[i].code == code1:
                        country = newAtlas.atlas[i].country

                currency = newEr._currencyInfo[country]

                print("Fuel cost between 2 airports:", cost, currency)

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
            exit()

        else:
            print("Sorry that was not a valid option, would you like to try again?")
            user_input = input("y/n?\n")

            if user_input == "n":
                user_input = 5



#main("/home/hugh/20230/project/data/airport.csv", "/home/hugh/20230/project/data/currencyrates.csv", "/home/hugh/20230/project/data/countrycurrency.csv")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
