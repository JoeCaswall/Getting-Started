# Running tests on a class

class AnonymousSurvey:
    """Collects anonymous answers to a survey question"""

    def __init__(self, quesiton):
        """Store a question and prepare to store responses"""
        self.question = quesiton
        self.responses = []
    
    def show_question(self):
        """Shows the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey"""
        self.responses.append(new_response)
    
    def show_results(self):
        """Display all stored results"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

