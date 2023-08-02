import requests

def get_weather_data():
    """
    Gets the weather data for a given city.

    Args:
        city: The name of the city.

    Returns:
        The weather data as a JSON object.
    """

    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(city)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
