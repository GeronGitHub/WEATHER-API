import requests
from apikeys import API_KEY
import math

# RETRIEVES THE COMPLETE DATA OF A GIVEN CITY
def getData(userCity):
    url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY + "&q=" + userCity
    response = requests.get(url)
    return response.json()

# RETRIEVES THE TEMPERATURE OF A GIVEN CITY IN DEGREES
def getTemperature(city):
    tempKelvin = getData(city)['main']['temp']
    tempCelsius = round(celsiusCalculator(tempKelvin))
    return getData(city)['name'] + " " + str(tempCelsius) + "°C"

# RETRIEVES THE WEATHER CONDITIONS OF A GIVEN CITY
def getCondition(city):
    mainCondition = getData(city)['weather'][0]['main']
    description = getData(city)['weather'][0]['description']
    return mainCondition, description

# CONVERTS TEMPERATURE FROM KELVIN TO DEGREES
def celsiusCalculator(kelvin):
    celsius = kelvin - 273.15
    return celsius

# HAVERSINE FORMULA - RETURNS THE DISTANCE BETWEEN TWO POINTS ON A SPHERE GIVEN THEIR LATITUDES AND LONGITUDES.
def haversineFormula(φ1, φ2, λ1, λ2):
    a = math.sin((φ2 - φ1) / 2)**2 + math.cos(φ1) * math.cos(φ2) * \
        math.sin((λ2 - λ1) / 2) * math.sin((λ2 - λ1) / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 6371 # RADIUS OF THE EARTH IN KM
    return R * c

#RETRIEVES THE DISTANCE BETWEEN TWO CITIES IN KM
def getDistanceBetweenTwoCities(cityOne, cityTwo):
    # lat REPRESENTS LATITUDE, long REPRESENTS LONGITUDE // DEGREES
    city1lat = getData(cityOne)['coord']['lat']
    city1long = getData(cityOne)['coord']['lon']
    city2lat = getData(cityTwo)['coord']['lat']
    city2long = getData(cityTwo)['coord']['lon']
    
    #CONVERTING FROM DEGREES TO RADIANS WHICH IS REQUIRED FOR THE DISTANCE CALCULATION
    # φ REPRESENTS LATITUDE, λ REPRESENTS LONGITUDE // RADIANS
    φ1 = city1lat * math.pi / 180 
    φ2 = city2lat * math.pi / 180
    λ1 = city1long * math.pi / 180
    λ2 = city2long * math.pi / 180
        
    return "The distance between " + getData(cityOne)['name'] + " and " + getData(cityTwo)['name'] + " is " + str(round(haversineFormula(φ1, φ2, λ1, λ2), 2)) + "km."

def runApp():
    
    choice = int(input("What would you like to know? \n\
    1. Temperature of a city\n\
    2. Distance between two cities\n\
    3. Weather condition of a city\n\
    4. Complete data of a city\n"))
    
    if choice == 1:
        citychosen = input("What city would you like to know the temperature of? ")
        print(getTemperature(citychosen))
    elif choice == 2:
        cityone, citytwo = input("Enter two cities: (type in this format -> city1, city2) ").split(",")
        print(getDistanceBetweenTwoCities(cityone, citytwo))
    elif choice == 3:
        citychosen = input("What city would you like to know the weather condition of? ")
        print(getCondition(citychosen))
    elif choice == 4:
        citychosen = input("What city would you like the complete data of? ")
        print(getData(citychosen))
    
    else:
        print("Please pick a number between 1 and 4!")
        runApp()
    
    return