import wordle

if __name__ == '__main__':
    while True:
        guessIt = wordle.Guess(
            w_str=input(">Input a 5 letter word\n>")
        )
        if guessIt.isValid():
            guessIt.increment()
            print(wordle.Guess.counter)
        else:
            print("Invalid word, try again")