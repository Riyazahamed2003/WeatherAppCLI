def get_data_by_date(data_list, date):
    """
    Gets the data for a given date from a list of weather data.

    Args:
        data_list: The list of weather data.
        date: The date to search for.

    Returns:
        The data for the given date, or None if the data is not found.
    """

    for data in data_list:
        if data["dt_txt"].startswith(date):
            return data
    return None
