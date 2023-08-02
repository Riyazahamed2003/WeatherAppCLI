def print_wind_speed(data):
    """
    Prints the wind speed for a given data object.

    Args:
        data: The data object.
    """

    if data:
        print(f"Wind Speed on {data['dt_txt']}: {data['wind']['speed']} m/s")
    else:
        print("No data found for the provided date.")
