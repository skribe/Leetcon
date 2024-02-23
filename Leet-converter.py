"""
Name:       Leet Converter
by:         skribe
Version:    3.1

Description:
    Reads a text file, converts all the alphabetical characters to leetcode, then writes new file with that converted leetcode
"""

# Leet converter

#imports
from sys import exit, argv
from random import choice

def main():

    # check if a correct amount has been parsed through command-line
    if len(argv) != 2:
        exit("Usage python Leet-coder.py <path/to/filename>")

    # constant
    TXT_FILE = argv[1]

    # tries to open input file.  If it fails then prints error to screen. 
    # if successful then does conversion
    try:
        with open(TXT_FILE, 'r') as f:
            line = f.readlines()

            # Converts input to leet
            leet_lines = do_lines(line)

        # writes to file leet-output.txt.  this will become user specifiable
        with open('leet-output.txt', 'a') as d:
            # prints out converted leet sentence
            d.writelines(leet_lines)

    # prints the error message if it fails
    except IOError as e:
        print(e)
        exit()


# Splits the sentence into words and adds them to the list 'words'
# iterates over the list and then sends each member to be encoded
# once encoded adds the encoded string to a new list 'leet_words'
def do_lines(line):
    leet_words = []

    for word in line:
        leet_word = leet_encoder(word)
        leet_words.append(leet_word)
    
    return leet_words


# does the conversion for each character into leet code
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

    # cycles through the characters in each word
    for c in unleet_word:

        # checks that the character is alphabetical
        if c.isalpha():
            leet_letter = choice(char_map[c.lower()])
            leet_word = leet_word + leet_letter
       
        # if not alphabetical then no conversion is done
        else:
            leet_word = leet_word + c
    
    return leet_word


if __name__ == "__main__":
    main()
