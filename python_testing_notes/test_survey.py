import pytest
from survey import AnonymousSurvey
# Fixtures help set up test envirinments, which often means creating a
# resource used by all tests (similar to beforeAll in JS)
# We can create a fixture by using the decorator @pytest.fixture
# A decorator is a directive placed just before a function definition
# which alters the behaviour of the function code.

@pytest.fixture
def language_survey():
    """A survey which will be available for all test functions"""
    question = "What is your first language?"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_single_survey_response(language_survey): # You need to pass the fixture as a parameter
    """Test that a single response is stored properly"""
    language_survey.store_response("English")
    assert "English" in language_survey.responses

def test_multiple_survey_responses(language_survey):
    """Test that multiple responses are stored properly"""
    responses = ["English", "Spanish", "Mandarin"]
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses
