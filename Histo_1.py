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

