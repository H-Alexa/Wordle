import wordle
import os

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
            w_str=input(">")
        )
        if guessIt.isValid():
            guessIt.applyGuess()
            guessIt.increment()
            #print(wordle.Guess.counter)
        else:
            print("Invalid word, try again")