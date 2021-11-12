#12.11.2021
#Konrad Brüggemann, Julia Mühlbruch

def histogram_characters_ger(input_sentence):
    sentence = input_sentence.lower()
    dict = {}
    for n in sentence:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(histogram_characters_ger("Die Studierenden klönen"))

def histogram_characters_en(input_sentence):
    sentence = input_sentence.lower()
    dict = {}
    sentence = sentence.replace("ö", "oe")
    sentence = sentence.replace("ü", "ue")
    sentence = sentence.replace("ä", "ae")
    sentence = sentence.replace("ß", "ss")
    for n in sentence:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(histogram_characters_en("Die Studierenden klönen"))

def histogramm_all_en(input_sentence):
    dict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    for letter in alphabet:
       dict[letter] = 0
    sentence = input_sentence.lower()
    sentence = sentence.replace("ö", "oe")
    sentence = sentence.replace("ü", "ue")
    sentence = sentence.replace("ä", "ae")
    sentence = sentence.replace("ß", "ss")
    for n in sentence:
        dict[n] += 1
    return dict
print(histogramm_all_en("Die Studierenden klönen"))

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
print(histogramm("Die Studierenden klönen"))