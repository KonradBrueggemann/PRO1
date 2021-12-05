from Tree import *


def test_case_1():
    an = Tree('eine', 0)  # IDs are unique and in arbitrary order
    idea = Tree('Idee', 1)
    sleeps = Tree('schlÃ¤ft', 2)

    det = Tree('DET', 3, [an])
    noun = Tree('N', 4, [idea])
    verb = Tree('V', 5, [sleeps])

    noun_phrase = Tree('NP', 6, [det, noun])
    verb_phrase = Tree('VP', 7, [verb])

    sentence = Tree('S', 8, [noun_phrase, verb_phrase])

    print(sentence)
    assert sentence.is_root()
    assert sentence.is_leaf() == False
    assert an.is_root() == False
    assert an.is_leaf()

    assert sentence.degree() == 2
    assert noun_phrase.degree() == 2
    assert verb_phrase.degree() == 1
    assert idea.degree() == 0

    print(sentence.pre_order())
    print(sentence.pre_order(by_label=True))
    print(sentence.pre_order(by_label=True, only_leaves=True))

    some_tree = Tree('S', 0, [])
    print(some_tree)
    assert some_tree.is_root()
    assert some_tree.is_leaf()


def test_case_2():
    some = Tree('manche', 0)  # IDs are unique and in arbitrary order
    ideas = Tree('Ideen', 1)
    will = Tree('werden', 2)
    never = Tree('niemals', 3)
    sleep = Tree('schlafen', 4)

    det = Tree('DET', 5, [some])
    noun = Tree('N', 6, [ideas])
    verb1 = Tree('V', 7, [will])
    adv = Tree('ADV', 8, [never])
    verb2 = Tree('V', 9, [sleep])

    noun_phrase = Tree('NP', 10, [det, noun])
    adv_phrase = Tree('ADV', 11, [verb1, adv])
    verb_phrase = Tree('VP', 12, [adv_phrase, verb2])

    sentence = Tree('S', 13, [noun_phrase, verb_phrase])

    print(sentence)
    print(sentence.pre_order())
    print(sentence.pre_order(by_label=True))
    print(sentence.pre_order(by_label=True, only_leaves=True))


if __name__ == "__main__":
    test_case_1()
    print(f'\n{"-" * 100}\n')
    test_case_2()