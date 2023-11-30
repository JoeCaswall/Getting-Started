# In tests we make assertions about what the value returned
# from a function SHOULD be.
# assert is similar to expect in Jest.

# the name of a test file, and the name of any test functions within it, 
# MUST start with 'test_' as this is what pytest
# looks for

from name_function import get_formatted_name


def test_first_last_name():
    """Do entries with no midle name's work?"""
    formatted_name = get_formatted_name("janis", "joplin")
    assert formatted_name == "Janis Joplin"

def test_first_middle_last_name():
    """Do entries with middle names work?"""
    formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
    assert formatted_name == "Wolfgang Amadeus Mozart"
# run the test with python3 -m -pytest #i've now swapped this to pytest using an alias

