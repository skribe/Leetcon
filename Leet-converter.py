# Leet converter

#imports
from sys import exit
from random import randint, random, choice

def main():
    # Version 2
    # - get sentence
    # - iterate through sentence
    # - splitting into individual words
    # ----> split words intto characters
    # ----> check to see if character alphabetical
    # ----> if alphabetical
    # --------> convert to leet
    # --------> add each leet character to leet word
    # ----> else add raw character
    # - recombine to create sentence
    # - output leet sentence
    
    try:
        while True:
            word = input("Sentence: ").lower().strip()
            if word.isalpha():
                leet_word = leet_encoder(word)
                print(leet_word)
                break
            else:
                raise ValueError
    except ValueError:
        exit("Invalid input")


def leet_encoder(unleet_word):
    char_map = {
        "a": ["4","@","^", "/\\"],
        "b": ["8", "|3"],
        "c": ["[", "(", "<"],
        "d": [")", "|)"],
        "e": ["3", "[-"],
        "f": ["ph", "|=", "v"],
        "g": ["6", "9", "C-"],
        "h": ["#", "|-|"],
        "i": ["|", "!"],
        "j": ["]", "_|"],
        "k": ["|<", "|c"],
        "l": ["|_", "1"],
        "m": ["nn", "11", "(v)"],
        "n": ["|\|", "^/"],
        "o": ["0", "()"],
        "p": ["|*", "|>"],
        "q": ["2", "0_"],
        "r": ["I2", "|?"],
        "s": ["5", "$", "z"],
        "t": ["7", "+"],
        "u": ["v", "|_|"],
        "v": ["\/", "|/"],
        "w": ["uu", "vv"],
        "x": ["][", ")("],
        "y": ["j", "`/"],
        "z": ["7_", "s"],
        }

    leet_word = ""

    for c in unleet_word:
        leet_letter = choice(char_map[c.lower()])
        leet_word = leet_word + leet_letter
    
    return leet_word


if __name__ == "__main__":
    main()
