from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('Who are you', "who are you",):
        return " I am Yee Chun Lok"

    return "I don't understand"