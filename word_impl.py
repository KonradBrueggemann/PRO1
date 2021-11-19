class Word:
    string_representation = "birne"

    def number_of_characters(word_input):
        x = len(word_input)
        return f"Das Wort '{word_input}' enthält {x} Zeichen."
    print(number_of_characters(string_representation))

    def capitalize(word_input):
        return word_input.capitalize()
    print(capitalize(string_representation))

    def get_ascii(word_input):
        ascii_value = ""
        for symbol in word_input:
            ascii_value += str(ord(symbol)) + " "
        return ascii_value
    print(get_ascii(string_representation))

    def histogramm(input_sentence, special_characters=False, count_all=True):
        sentence = input_sentence.lower()
        dict = {}
        if special_characters:
            sentence = sentence.replace("ö", "oe")
            sentence = sentence.replace("ü", "ue")
            sentence = sentence.replace("ä", "ae")
            sentence = sentence.replace("ß", "ss")
        if count_all:
            alphabet = "abcdefghijklmnopqrstuvwxyz "
            for letter in alphabet:
                dict[letter] = 0
        for n in sentence:
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
        return dict

    print(histogramm(string_representation))