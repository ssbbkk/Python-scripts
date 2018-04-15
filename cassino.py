import random

class Greeter(object):
# Initialization function
    def __init__(self, name):
        self.name = name

# Other functions
    def hello(self):
        print("Hello " + self.name)

    def goodbye(self):
        print("Goodbye " + self.name)

# Creating an instance (named "g") of class Greeter
g = Greeter("Henry")
g.hello()
g.goodbye()

g2 = Greeter("Adam")
g2.hello()
g2.goodbye()
