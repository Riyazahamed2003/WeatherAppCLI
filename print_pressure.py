def print_pressure(data):
    """
    Prints the pressure for a given data object.

    Args:
        data: The data object.
    """

    if data:
        print(f"Pressure on {data['dt_txt']}: {data['main']['pressure']} hPa")
    else:
        print("No data found for the provided date.")
