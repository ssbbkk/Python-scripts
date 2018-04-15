# This file contain some function examples

def starts_with_vowel(word):
    return word[0] in "aeiouyAEIOUY"

friends = ["Monica", "Joe", "Rachel", "Phoebe", "Chandler", "Ross"]

def filter_names(name):
    names_vowel = []
    for i in name:
        if starts_with_vowel(word):
            names_vowel.append(word)
    return names_vowel

v = filter_names(friends)

print(str(v))
