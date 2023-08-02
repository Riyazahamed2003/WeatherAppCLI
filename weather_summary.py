import json

def print_weather_summary(weather_data):
    for data in weather_data['list']:
        print(f"Date/Time: {data['dt_txt']}, Temperature: {data['main']['temp']:.2f}°C, Weather Description: {data['weather'][0]['description']}, Wind Speed: {data['wind']['speed']} m/s, Pressure: {data['main']['pressure']} hPa, Weather Icon: {data['weather'][0]['icon']}")
