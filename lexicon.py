# Lexicon.py
# Original 09 SEP 2016
# Aktuelle Version 06 DEC 2021
# MP, JG, SS


from arpabet_to_sampa import ARPABET2SAMPA

# class that handles phonetic lexicons


class Lexicon:
    def __init__(self, language, filename):
        self.language = language
        self.lex = self.read_lexicon_file(filename)
        self.NumberOfChanges = 0

    def __str__(self):
        return str(self.language) \
               + "\t" \
               + str(len(self.lex.keys())) \
               + " entries"

    def read_lexicon_file(self, filename):
        lex_dict = {}

        with open(filename, "r", encoding="latin-1", errors="ignore") as f:
            for line in f:
                if not line.startswith(";;;") and "(" not in line:
                    item = line.strip("\n").split(" ")
                    # remove empty elements
                    item = [x for x in item if x != ""]
                    lex_dict[item[0].lower()] = item[1:]
        return lex_dict

    def get_sound_inventory(self):
        """ returns a list of all sounds in lexicon. """
        sounds = [s for token in list(self.lex.keys())
                  for s in self.lex[token]]
        sounds = list(set(sounds))
        sounds.sort()
        return sounds

    def onsets(self):
        """ print out all onsets. """
        onsets = []
        for token, pron in self.lex.items():
            while pron[0] in ('"', '""', '%', chr(164)):
                pron = pron[1:]
            onset = []
            i = 0
            # everything that comes before the first vowel is in the onset
            # disregard stress markers
            while i < len(pron) and \
                    pron[i] not in ('$', '_') and \
                    pron[i] not in self.vowels() and \
                    pron[i] not in self.diphthongs():
                onset.append(pron[i])
                i += 1
            if len(onset):
                onsets.append(''.join(onset))
        onsets = list(set(onsets))
        onsets.sort()
        return onsets

    def phonemes(self):
        """
        returns a dictionary of all english phonemes
        and their classification.
        """
        if self.language == "eng":
            return ARPABET2SAMPA

    def consonants(self):
        return [c for c in self.phonemes() if self.phonemes()[c] == "c"]

    def vowels(self):
        return [v for v in self.phonemes() if self.phonemes()[v] == "v"]

    def diphthongs(self):
        return [d for d in self.phonemes() if self.phonemes()[d] == "d"]

    def apply_error_pattern(self, pattern):
        """
        :param pattern: type of error pattern
        :return: calls respective function
        """
        pattern = pattern.lower()
        if pattern == "velar_fronting":
            self.velar_fronting()
        elif pattern == "coronal_backing":
            self.coronal_backing()
        elif pattern == "stopping":
            self.stopping()
        elif pattern == "gliding":
            self.gliding()
        elif pattern == "r_weakening":
            self.r_weakening()
        elif pattern == "final_consonant_deletion":
            self.final_consonant_deletion()
        elif pattern == "delete_pretonic_syllable":
            self.delete_pretonic_syllable()

    def velar_fronting(self):
        self.NumberOfChanges += 1
        self.replace_sound("k", "t")
        self.replace_sound("g", "d")
        self.replace_sound("N", "n")

    def coronal_backing(self):
        self.NumberOfChanges += 1
        self.replace_sound("t", "k")
        self.replace_sound("d", "g")
        self.replace_sound("n", "N")

    def stopping(self):
        self.NumberOfChanges += 1
        self.replace_sound("f", "p")
        self.replace_sound("v", "b")
        self.replace_sound("s", "t")
        self.replace_sound("S", "t")
        self.replace_sound("tS", "t")
        self.replace_sound("z", "d")
        self.replace_sound("Z", "d")
        self.replace_sound("dZ", "d")
        self.replace_sound("T", "p")
        self.replace_sound("D", "b")

    def gliding(self):
        self.NumberOfChanges += 1
        self.replace_sound("r", "w")
        self.replace_sound("l", "j")

    def r_weakening(self):
        self.NumberOfChanges += 1
        self.replace_sound("r", "j")

    def final_consonant_deletion(self):
        """ deletes final consonant. """
        for token in self.lex.keys():
            if self.lex[token][-1] in self.consonants():
                self.lex[token] = self.lex[token][:-1]

    def delete_pretonic_syllable(self):
        """ deletes everything before a quotation mark. """
        for token in self.lex.keys():
            i = self.lex[token].index("\"")
            self.lex[token] = self.lex[token][i:]

    def replace_sound(self, old, new):
        """ replaces old sound with new sound """
        self.NumberOfChanges += 1
        for token in self.lex.keys():
            if old in self.lex[token]:
                new_trans = []
                for p in self.lex[token]:
                    if p == old:
                        new_trans.append(new)
                    else:
                        new_trans.append(p)
                self.lex[token] = new_trans


def main():
    lexicon = Lexicon('eng', 'cmudict-0.7b')
    phonemes = lexicon.get_sound_inventory()
    print(len(phonemes))
    lexicon.apply_error_pattern('stopping')
    print('{} sounds have been changed.'.format(lexicon.NumberOfChanges))
    print('{} onsets'.format(len(lexicon.onsets())))


main()