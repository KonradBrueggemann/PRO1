from Histo_1 import histogramm
# Aufgabe 1 - Magic Methods
class Word:
    string_representation = ""

    def __init__(self, string):
        """
        Set-Operation. Initializes an
        instance of the Word class taking
        a string argumenr for the internal
        strin_representation state.
        """
        self.string_representation = string

    def number_of_characters(self):
        """
        Get-Operation. Returns a string containing
        the value of string_representation and the
        number of letters in it.
        """
        return "Das Wort '{}' enthält {} Zeichen." \
            .format(self.string_representation, len(self.string_representation))

    def capitalize(self):
        """
        Get-Operation. Returns a string containing
        the capitalized version
        of the string_representation.
         """
        return self.string_representation.title()

    def get_ascii(self):
        """
        Get-Operation. Returns a string containing
        the ASCII version of string_representation.
        """
        string_ascii = []
        for letter in self.string_representation:
            string_ascii.append(str(ord(letter)))
        return " ".join(string_ascii)

    def histrogram(self, ):
        """
        Get-Operation. Returns a dictionary
        containing a histogramm for the
        letter frequency in string_representation.
        """
        return histogramm(self.string_representation)

    def __str__(self):
        """
        No conditions given.
        """
        return str(self.string_representation)
    def __len__(self):
        """

        Precondition:
        Object cant be an integer or boolean
        """
        return len(self.string_representation)
    def __add__(self, other):
        """
        Precondition:
        Both objects have to be a string.
        """
        assert type(self) == Word
        return str(self.string_representation+" "+other)
    def __reversed__(self):
        """

        Precondition:
        has to be string or a list.
        """
        return self.string_representation[::-1]


w1 = Word("blume")
w2 = Word("Sonnenfinsternis")


print(w1.number_of_characters())
print(w1.capitalize())
print(w1.get_ascii())
print(w1.histrogram())

print(w2.number_of_characters())
print(w2.capitalize())
print(w2.get_ascii())
print(w2.histrogram())
print(w2.__str__())
print(w2.__len__())
print(w2.__add__(w1.__str__()))
print(w2.__reversed__())

#Aufgabe 2
def test_cases():
    assert w1.__str__() == "blume"
    assert w2.__str__() == "Sonnenfinsternis"
    assert w1.__len__() == 5
    assert w2.__len__() == 16
    assert w1.__add__(w2.__str__()) == "blume Sonnenfinsternis"
    assert w2.__add__(w1.__str__()) == "Sonnenfinsternis blume"
    assert w1.__reversed__() == "emulb"
    assert w2.__reversed__() == "sinretsnifnennoS"
if __name__ == "__main__":
    test_cases()