def city_country(city, country, population=None):
    """returns a string containing a city and its country"""
    if population:
        location = f"{city}, {country} - population {population}"
        return location.title()
    else:
        location = f"{city}, {country}"
        return location.title()