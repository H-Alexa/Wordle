import wordle
import os
import sys

os.system("cls") if os.name == "nt" else os.system("clear")

begin_message = """
'##:::::'##::'#######::'########::'########::'##:::::::'########:
 ##:'##: ##:'##.... ##: ##.... ##: ##.... ##: ##::::::: ##.....::
 ##: ##: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##::::::: ##:::::::
 ##: ##: ##: ##:::: ##: ########:: ##:::: ##: ##::::::: ######:::
 ##: ##: ##: ##:::: ##: ##.. ##::: ##:::: ##: ##::::::: ##...::::
 ##: ##: ##: ##:::: ##: ##::. ##:: ##:::: ##: ##::::::: ##:::::::
. ###. ###::. #######:: ##:::. ##: ########:: ########: ########:
:...::...::::.......:::..:::::..::........:::........::........::
"""
begin_message = begin_message.replace("#", f"{wordle.Color.GREEN}O{wordle.Color.BASE}")
#begin_message = begin_message.replace(".", f"{wordle.Color.YELLOW}.{wordle.Color.BASE}")
print(begin_message)
print("Input a 5 letter word (in lowercase) to begin \n")
if __name__ == '__main__':
    with open("cheat.txt","w") as f:
        f.write(wordle.CHOSEN)
    while True:
        guessIt = wordle.Guess(
            w_str=input(f"[{wordle.Guess.counter}]>")
        )
        if guessIt.w_str == "h":
            listValue = list(wordle.Guess.alphabet.values())
            for element in listValue:
                if listValue[-1]!= element:
                    print(element,end=" ")
                else :
                    print(element)
            continue
        if guessIt.isValid():
            guessIt.applyGuess()
            guessIt.wincheck()
            guessIt.increment()
            guessIt.losscheck()
            #print(wordle.Guess.counter)
        else:
            print("Invalid word, try again")