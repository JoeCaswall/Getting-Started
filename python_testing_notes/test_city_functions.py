from city_functions import city_country

def test_city_country():
    """Does it return the correct string with no population given?"""
    location = city_country("london", "england")
    assert location == "London, England"

def test_city_country_pop():
    """Does it also work when a population is given?"""
    location = city_country("london", "england", 10000000)
    assert location == "London, England - Population 10000000"