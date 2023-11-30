def get_formatted_name(first, last, middle=""):
    """Generates a neatly formatted name"""
    if middle:
        full_name = f"{first} {middle} {last}"
        return full_name.title()
    else:
        full_name = f"{first} {last}"
        return full_name.title()
