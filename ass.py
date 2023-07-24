# QA Engineer Intern_Assignment @Nimesa Technologies

import requests
import json

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather(date):
    response = requests.get(url)
    data = json.loads(response.content)
    temp = data['list'][0]['main']['temp']
    return temp

def get_wind_speed(date):
    response = requests.get(url)
    data = json.loads(response.content)
    wind_speed = data['list'][0]['wind']['speed']
    return wind_speed

def get_pressure(date):
    response = requests.get(url)
    data = json.loads(response.content)
    pressure = data['list'][0]['main']['pressure']
    return pressure

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date: ")
            temp = get_weather(date)
            print("The temperature on {} is {} degrees Celsius".format(date, temp))
        elif choice == 2:
            date = input("Enter the date: ")
            wind_speed = get_wind_speed(date)
            print("The wind speed on {} is {} meters per second".format(date, wind_speed))
        elif choice == 3:
            date = input("Enter the date: ")
            pressure = get_pressure(date)
            print("The pressure on {} is {} hPa".format(date, pressure))
        elif choice == 0:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
