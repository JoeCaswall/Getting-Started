from survey import AnonymousSurvey

# Define a question and create a survey

question = "What is your first language?"

language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("Enter 'q' at any time to quit")
while True:
    response = input("Language: ")
    if response == "q":
        break
    language_survey.store_response(response)

print("\nThank you to all who participated!")
print("Results:")
language_survey.show_results()