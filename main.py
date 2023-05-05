import api_project as app

print("\nWELCOME TO GERON'S CITY API !\n")

continueLoop = 'Y'
while continueLoop == 'Y':

    choice = int(input("What would you like to know? \n\
    1. Temperature of a city\n\
    2. Distance between two cities\n\
    3. Weather condition of a city\n\
    4. Complete data of a city\n"))


    if choice == 1:
        citychosen = input("What city would you like to know the temperature of? ")
        print(app.getTemperature(citychosen))
    elif choice == 2:
        cityone, citytwo = input("Enter two cities: (type in this format -> city1, city2) ").split(",")
        print(app.getDistanceBetweenTwoCities(cityone, citytwo))
    elif choice == 3:
        citychosen = input("What city would you like to know the weather condition of? ")
        print(app.getCondition(citychosen))
    elif choice == 4:
        citychosen = input("What city would you like the complete data of? ")
        print(app.getData(citychosen))
    
    continueChoice = input("Do you want to continue? (Y/N) ").upper()
    continueLoop = continueChoice


