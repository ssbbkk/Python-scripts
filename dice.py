import random

class Dice(object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class Deck(object):
    def shuffle(self):
        suits = ['S', 'D', 'H', 'C']
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = []		# Add self. before list name to be albe to use it outside the class
        for suit in suits:
            for rank in ranks:
                self.cards.append(rank + " " + suit)

        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()		# Function .pop() removes selected object from the list, here removed cards will not be dealed again 

d = Deck()
d.shuffle()
print("\nP1    : [" + d.deal() + "] " + " [" + d.deal() + "] \n")
print("P2    : [" + d.deal() + "] " + " [" + d.deal() + "] \n")

d.deal()
print("Flop  : [" + d.deal() + "]" + " [" + d.deal() + "]" + " [" + d.deal() + "]    Turn  : [" + d.deal() + "]   River : [" + d.deal() + "]\n")

#print("D64 rolls:")
#d = Dice(64)
#print(d.roll())


#print("D128 rolls:")
#d2 = Dice(128)
#print(d2.roll())

