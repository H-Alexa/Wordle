import wordle, help
import os, sys
import argparse

begin_message = """
'##:::::'##::'#######::'########::'########::'##:::::::'########:
 ##:'##: ##:'##.... ##: ##.... ##: ##.... ##: ##::::::: ##.....::
 ##: ##: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##::::::: ##:::::::
 ##: ##: ##: ##:::: ##: ########:: ##:::: ##: ##::::::: ######:::
 ##: ##: ##: ##:::: ##: ##.. ##::: ##:::: ##: ##::::::: ##...::::
 ##: ##: ##: ##:::: ##: ##::. ##:: ##:::: ##: ##::::::: ##:::::::
. ###. ###::. #######:: ##:::. ##: ########:: ########: ########:
:...::...::::.......:::..:::::..::........:::........::........::
""".replace("#", f"{wordle.Color.GREEN}{wordle.Color.BOLD}O{wordle.Color.BASE}").replace(".", f"{wordle.Color.YELLOW}{wordle.Color.BOLD}.{wordle.Color.BASE}")

instruction = help.how_to_play
instruction = instruction.replace("WORDLE", f"{wordle.Color.BOLD}WORDLE{wordle.Color.BASE}")
instruction = instruction.replace("green", f"{wordle.Color.GREEN}{wordle.Color.BOLD}green{wordle.Color.BASE}")
instruction = instruction.replace("yellow", f"{wordle.Color.YELLOW}{wordle.Color.BOLD}yellow{wordle.Color.BASE}")
instruction = instruction.replace("grey", f"{wordle.Color.GREY}{wordle.Color.BOLD}grey{wordle.Color.BASE}")


def start():
    os.system("cls") if os.name == "nt" else os.system("clear")

    print(begin_message)
    print(instruction)
    print("Input a 5 letter word (in lowercase) to begin \n")


def main():
    start()

    while True:
        guessIt = wordle.Guess(
            w_str=input(f"[{wordle.Guess.counter}]>")
        )
        if guessIt.w_str == "h":
            listValue = list(wordle.Guess.alphabet.values())
            for element in listValue:
                if listValue[-1]!= element:
                    print(element,end=" ")
                else:
                    print(element)
            continue
        if guessIt.isValid():
            guessIt.applyGuess()
            guessIt.wincheck()
            guessIt.increment()
            guessIt.losscheck()
            if args.debug:
                print(wordle.Guess.counter)
        else:
            print("Invalid word, try again")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser = argparse.ArgumentParser(
            description=help.how_to_play,
            epilog='Best of luck!'
        )

    parser.add_argument('--debug', action='store_true', help='Launch in debug mode. Additional verbose, plus the guessed word gets added to cheat.txt')

    args = parser.parse_args()

    if args.debug:
        with open("cheat.txt","w") as f:
            f.write(wordle.CHOSEN)

    main()
