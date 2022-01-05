from chatbot import chatbot
from user_data import user_data
import nltk
import random
from nltk.stem import WordNetLemmatizer

class interface:
    message = "Merry Christmas! I welcome you to your personal X-mas assistant for this season, say hello ^^"
    print(message)
    lemmatizer = WordNetLemmatizer
    run = True
    user_info = user_data(age=None,
                          name=None,
                          tradition=None,
                          santa=None,
                          colour=None,
                          season=None)
    while run:
        user_input = input()
        user_tokens = nltk.word_tokenize(user_input.lower())
        for intent in chatbot.bot_data["intents"]:
            match = False
            x = 0
            for token in user_tokens:
                if token in chatbot.bag_of_words(intent["patterns"]):
                    x += 1
            if x > (len(user_tokens)/1.75):
                match = True
                break
        if match:
            if intent["tag"] == "goodbye":
                exit(random.choice(intent["responses"]))
            print(random.choice(intent["responses"]))
            for attribute in user_info.attributes():
                if user_info.attributes()[attribute] is None:
                    question_type = attribute
                    question = chatbot.bot_questions[question_type]
                    answer = input(question + "\n")
                    if question_type == "name":
                        user_info.name = answer
                    if question_type == "age":
                        user_info.age = answer
                    if question_type == "tradition":
                        user_info.tradition = answer
                    if question_type == "santa":
                        user_info.santa = answer
                    if question_type == "colour":
                        user_info.colour = answer
                    if question_type == "season":
                        user_info.season = answer
                    print(random.choice(chatbot.bot_reactions))
                    break
        if not match:
            print("I have no idea what you are trying to say.")