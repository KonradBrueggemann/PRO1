from word_impl import Word
class Sentence:
    string_representation = ""

    def assert_input(self):
        count = 0
        for i in str(self):
            if i == " ":
                count += 1
        assert count >= 2
        return self

    def __init__(self, string):
        """
        Set-Operation. Initializes an
        instance of the Word class taking
        a string argumenr for the internal
        strin_representation state.
        """
        self.string_representation = string

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

    def tokenize(self):
        result = []
        for element in [word_imply for word_imply in self.string_representation.split()]:
            result.append(Word(element))
        return result


w1 = Sentence("Karl")
w2 = Sentence("Karl steigt auf das Dach")

# Test Cases

for word in w2.assert_input().tokenize():
    print(word.__add__(w2.__str__()))

for word in w2.assert_input().tokenize():
    print(word.get_ascii())