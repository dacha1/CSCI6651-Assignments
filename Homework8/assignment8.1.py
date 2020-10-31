import random
class Animal():
    def __init__(self, ani_type, name):
        self.ani_type = ani_type
        self.name = name
        self.guessestaken = 0
        self.guess = None
