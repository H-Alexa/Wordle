import random
import sys
from validWords import valid 

CHOSEN = random.choice(valid)
CHANCES = 6

class Color:
    PREFIX = '\033'
    BASE = "\033[0m"
    GREY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BOLD='\033[1m'
    ITALIC='\033[3m'


class Guess:
    counter = 1
    words = []
    alphabet = {    
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
        }

    def __init__(self,w_str:str):
        self.w_str = w_str
        self.w_chars = list(self.w_str)
        self.post_guess_w_str = ""

    def increment(self):
        Guess.counter += 1
    def isValid(self):
        return self.w_str in valid


    def applyGreens(self):
        for i,_ in enumerate(self.w_chars):
            actualChar = CHOSEN[i]
            guessedChar = self.w_chars[i]
            if actualChar == guessedChar:
                colored =  f"{Color.GREEN}{actualChar}{Color.BASE}"
                self.w_chars[i] = colored
                self.editAlpha(actualChar,colored)
    
    def applyYellows(self):
        for i, _ in enumerate(self.w_chars):
            guessedChar = self.w_chars[i]
            notInGreen = Color.GREEN not in Guess.alphabet.get(guessedChar, "")
            if guessedChar in CHOSEN:
                colored = f"{Color.YELLOW}{guessedChar}{Color.BASE}"
                self.w_chars[i] = colored
                if notInGreen:
                    self.editAlpha(guessedChar,colored)
            else:
                colored = f"{Color.RED}{guessedChar}{Color.BASE}"
                self.editAlpha(guessedChar,colored)

    
    def editAlpha (self,k,d):
        if k not in Guess.alphabet.keys():
            return
        Guess.alphabet[k] = d

    def applyGuess(self):
        self.applyGreens()
        self.applyYellows()
        self.post_guess_w_str="".join(self.w_chars)
        Guess.words.append(self.post_guess_w_str)
        print(self.post_guess_w_str)

    def wincheck(self):
        if self.w_str == CHOSEN:
            print(f"Congratulations! You succeded at {Guess.counter}th attempt")
            for element in Guess.words:
                print(element)
            sys.exit(0)


    def losscheck(self):
        if self.counter == CHANCES+1:
            print(f"Sorry, you lost. The word was {CHOSEN}")
            sys.exit(0)
