"""
Name:       Leet Converter
by:         skribe
Version:    2

Description:
    Takes a string and prints out the corresponding leetcode
"""

# Leet converter

#imports
from sys import exit
from random import choice

def main():
    # Version 2
    # - get sentence
    # - iterate through sentence
    # - splitting into individual words
    # ----> split words into characters
    # ----> check to see if character alphabetical
    # ----> if alphabetical
    # --------> convert to leet
    # --------> add each leet character to leet word
    # ----> else add raw character
    # - recombine to create sentence
    # - output leet sentence
    
    # Checks for valid input
    while True:
        try:
            sentence = input("Sentence: ").lower().strip()
            break
        except ValueError:
            exit("Invalid input")

    # Converts input to leet
    leet_sentence = do_sentence(sentence)

    # prints out converted leet sentence
    print(' '.join(leet_sentence))


# Splits the sentence into words and adds them to the list 'words'
# iterates over the list and then sends each member to be encoded
# once encoded adds the encoded string to a new list 'leet_words'
def do_sentence(sentence):
    leet_words = []
    words = sentence.split()
    for word in words:
        leet_word = leet_encoder(word)
        leet_words.append(leet_word)
    
    return leet_words



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
        if c.isalpha():
            leet_letter = choice(char_map[c.lower()])
            leet_word = leet_word + leet_letter
        else:
            leet_word = leet_word + c
    
    return leet_word


if __name__ == "__main__":
    main()
