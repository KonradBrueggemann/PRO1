# Weihnachtsprojekt
# Konrad Brüggemann, Julia Mühlbruch
# 05.12.2021
import nltk
import random

class chatbot:
    bot_data = {"intents": [
        {"tag": "greetings",
        "patterns": ["hello", "hi", "hey", "yo", "howdy partner", "wassup", "whats up"],
         "responses": ["Hello!", "Hey :D", "WAZZUP!!!", "Hi^^", "Howdy", "*steals your christmas gifts*"]},

        {"tag": "goodbye",
         "patterns": ["goodbye", "g2g", "bye", "see you soon", "i'm heading off", "cya"],
         "responses": ["I never want to see you again", "You are leaving already?</3", "Bye", "GN", "Talk to you later!"]},

        {"tag": "name",
         "patterns": ["who are you", "whats your name?", "what are you?", "what should i call you?"],
         "responses": ["You can call me Rudolph the friendly X-mas Bot!", "I am Rudolph, your X-mas Bot *beep boop*", "I am Rudolph :^)"]},

        {"tag": "age",
         "patterns": ["how old?", "how old is rudolph?", "how old are you?", "age?"],
         "responses": ["My owner Santa Claus is over 10,000 years old therefore I am 1 year old :D", "I am 1!","1 year old :^)"]},

        {"tag": "purpose",
         "patterns": ["what goal do you have?", "what is your purpose?", "what is your intention?"],
         "responses": ["I am here to assist you during your holidays so that you can have a flawless christmas!", "I am here to talk to you about christmas, ask me anything^^"]},

        {"tag": "gifts",
         "patterns": ["how many gifts will i get", "gifts", "gift amount", "what is my gift count?", "i wanna now how many gifts i will get"],
         "responses": [f"You will receive {random.randint(0,10)} gifts."]},

        {"tag": "reindeer",
         "patterns": ["isn't rudolph a reindeer?", "aren't you a reindeer?", "why are you named after a reindeer?"],
         "responses": ["My colleague is Rudolph the Reindeer, I am just the digital assistant of Mr.Claus", "I am the digital assistant Rudolph, there is also the leading Reindeer Rudolph. Two Worlds my friend"]},

        {"tag": "options",
         "patterns": ["what are my options", "what can you do?"],
         "responses": ["I can sing for you, send you a picture of a christmas tree, determine if you were nice or naughty or how tell you how many gifts you will receive this season!"]},

        {"tag": "sing",
         "patterns": ["sing for me", "do you know any popular christmas songs?", "sing", "last christmas"],
         "responses": ["Last Christmas, I gave you my heart. But the very next day, you gave it away. This year, to save me from tears, I'll give it to someone special~...<3"]},

        {"tag": "send",
         "patterns": ["send me a pic of a christmas tree", "send me a cool tree", "send", "christmas tree please"],
         "responses": ["*cringe Mario voice* Here you go: https://i.dailymail.co.uk/i/pix/2017/12/05/15/470314D900000578-5148009-image-m-45_1512488839989.jpg", "Here is one heckin tree >:^): https://i.pinimg.com/originals/2b/1c/3e/2b1c3e42d15484b4465348cc0880d0e3.jpg", "Here :^):https://s3.awkwardfamilyphotos.com/wp-content/uploads/2016/12/22153517/tree-e1480630056438.jpg"]},

        {"tag": "nice or naughty",
         "patterns": ["was i nice or naughty?"],
         "responses": ["Oh you were definitely naughty this year ( ˶˘ ³˘(˵ ͡° ͜ʖ ͡°˵)♡", "Oh you were such a nice human this year, Mr.Claus is very proud of you (づ｡◕‿‿◕｡)づ"]},

        {"tag": "mood",
         "patterns": ["how have you been", "how are you doing", "whats up", "how is it going"],
         "responses": ["I am fine, thank you for asking :^)", "I am alright^^", "I hate my life, but that is beside the point..", "Its fine, you know how life is :,)", "Could not be better <3"]},
    ]}
    bot_questions = {"age": "By the way, how old are you?", "name": "May I ask what your name is?", "tradition": "What is your favorite Christmas Tradition?", "santa":"Do you believe in Santa?", "colour": "What is your favorite colour?", "season": "What is your favorite season?"}
    bot_reactions = ["Nice ", "Sucks to be you ಠ_ಠ", "You must be fun in parties (ノ﹏ヽ)", "That's nice, I guess (´･ω･`).", "That's what we would call an epic gamer moment (・ε・｀)", "Same ( ‘́⌣’̀)/(˘̩̩ε˘̩ƪ)"]
    @staticmethod
    def bag_of_words(pattern):
        bag = []
        for sentence in pattern:
            tokens = nltk.word_tokenize(sentence)
            for token in tokens:
                bag.append(token)
        return bag
