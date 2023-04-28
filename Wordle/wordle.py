import random
from validWords import valid 

CHOSEN = random.choice(valid)
CHANCES = 7

class Guess:
    counter = 1
    def __init__(self,w_str:str):
        self.w_str = w_str
        self.w_chars = list(self.w_str)

    def increment(self):
        Guess.counter += 1
    def isValid(self):
        return self.w_str in valid
