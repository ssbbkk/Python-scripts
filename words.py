import scrabble

letters = "abcdefghijklmnopqrstquwxyz"

def has_a_double(letter):
    for word in scrabble.wordlist:
        if letter + letter in word:
            return True
    return False

for letter in letters:
    if not has_a_double(letter):
        print(letter + " never appeard doubbled")

# Print all words containing letters in " " statement
#for word in scrabble.wordlist:
#    if "aa" in word and "ee" in word:
#        print(word)
