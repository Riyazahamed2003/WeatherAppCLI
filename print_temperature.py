def print_temperature(data):
    """
    Prints the temperature for a given data object.

    Args:
        data: The data object.
    """

    if data:
        print(f"Temperature on {data['dt_txt']}: {data['main']['temp']} °K")
    else:
        print("No data found for the provided date.")
