# mad-libs.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 8 Project

import os
import re

def madLibs(input_file, output_file):
    """lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file
    Args:
        filename (str): name of file to parse
    Returns:
        None
    """
    regex = re.compile(r'\w*(NOUN|ADJECTIVE|ADVERB|VERB)\w*')

    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:

        words = in_file.read().split(' ')
        result = []

        for w in words:

            mo = regex.search(w)

            if mo:
                match = mo.group(1)
                print(f'Enter a {match.lower()}: ', end='')
                i = input()
                result.append(regex.sub(i, w))
            else:
                result.append(w)
   
        result = ' '.join(result)

        out_file.write(result)
        print(result)


if __name__ == "__main__":
    madLibs('input.txt', 'output.txt')
