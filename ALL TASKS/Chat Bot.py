import random
class Chatbot:
    def __init__(self):
        self.rules = {
            'greet': ['hello', 'hi', 'hey'],
            'ask_name': ['what\'s your name', 'what is your name', 'what name'],
            'ask_weather': ['what is the weather', 'what is the weather today', 'what weather'],
            'goodbye': ['goodbye', 'bye', 'see you'],
            'default': ['i didn\'t understand', 'can you repeat', 'sorry']
        }
        self.responses = {
            'greet': ['Hello! Nice to meet you.', 'Hi! How can I help you today?'],
            'ask_name': ['My name is Chatbot.', 'I am Chatbot.'],
            'ask_weather': ['I\'m just a chatbot, I don\'t have real-time access to the weather.'],
            'goodbye': ['Goodbye! See you next time.', 'Bye! Have a nice day.'],
            'default': ['I didn\'t understand your query.Please rephrase your question.','Can you please repeat your question?']
        }

    def respond(self, user_input):
        user_input = user_input.lower()
        for key, values in self.rules.items():
            if any(value in user_input for value in values):
                return random.choice(self.responses[key])
        return random.choice(self.responses['default'])

chatbot = Chatbot()
while True:
    user_input = input("User: ")
    response = chatbot.respond(user_input)
    print("Chatbot: ", response)

