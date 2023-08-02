def get_option_from_user():
    """
    Gets the option from the user.

    Returns:
        The option as a string.
    """

    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")
    option = input("Enter your option: ")
    return option
