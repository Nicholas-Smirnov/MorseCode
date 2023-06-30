import winsound
import time

MorseAlphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "!": "-.-.--",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "/": "-..-.",
    "@": ".--.-.",
    " ": " "

}

def soundOutMessage(message):
    for letter in message:
        if letter == " ":
            print(" ")
        else:
            print(MorseAlphabet[letter.upper()])
            for morseLetter in MorseAlphabet[letter.upper()]:
                if morseLetter == ".":
                    winsound.Beep(440, 100)
                elif morseLetter == "-":
                    winsound.Beep(440, 300)
                else:
                    print("Error")
            print(" ")
            time.sleep(0.4)


def main():
    message = input("Enter a message: ")
    soundOutMessage(message)

main()
