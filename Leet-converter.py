"""
Name:       Leet Converter
by:         skribe
Version:    3.2

Description:
    Reads a text file, converts all the alphabetical characters to leetcode, then writes new file with that converted leetcode
"""

# Leet converter

#imports
from sys import exit, argv
from random import choice
import argparse


def main():

    # check if a correct options have been parsed through command-line
    parser = argparse.ArgumentParser()
    parser.add_argument('source_file', metavar='source', help='Input filename')
    parser.add_argument('dest_file', metavar='dest', help='Output filename')
    args = parser.parse_args()
        
    # constant
    INPUT_FILE = args.source_file
    OUTPUT_FILE = args.dest_file

    # tries to open input file.  If it fails then prints error to screen. 
    # if successful then does conversion
    try:
        with open(INPUT_FILE, 'r') as i:
            line = i.readlines()

            # Converts input to leet
            leet_lines = do_lines(line)

        # writes to file leet-output.txt.  this will become user specifiable
        with open(OUTPUT_FILE, 'a') as o:
            # prints out converted leet sentence
            o.writelines(leet_lines)

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
