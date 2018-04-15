import scrabble

letters = "abcdefghijklmnopqrstquwxyz"
vowel = "aeiou"

def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True

counter = 0
for word in scrabble.wordlist:
    if has_all_vowels(word):
        counter = counter + 1
        print(word)
print(counter)
