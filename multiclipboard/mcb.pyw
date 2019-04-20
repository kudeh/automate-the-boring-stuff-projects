#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')


if len(sys.argv) == 3: 
    # Save & Delete clipboard content.

    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()

    elif sys.argv[1].lower() == 'delete':

        if sys.argv[2]:                      # Delete key
            del mcbShelf[sys.argv[2]]      
            pyperclip.copy('')


elif len(sys.argv) == 2:  
    # List, Delete all keywords and load content.

    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))

    elif sys.argv[1].lower() == 'delete':
        for key in list(mcbShelf.keys()):
            del mcbShelf[key]
        pyperclip.copy('')

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

if __name__ == "__main__":
    pass