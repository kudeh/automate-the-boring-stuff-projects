#! python3
# selective-copy.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 9 Project

import os, shutil

def selectiveCopy(inputFolder, ext, outputFolder):
    """Walks through a folder tree and searches for files with a certain file extension, copies them into new folder
    Args:
        inputFolder (str): Path of folder to search in
        ext (str): file extension to search for
        outputFolder (str): Path of folder to copy files into
    Returns:
        None
    """

    resultFolder = os.path.abspath(outputFolder)
    #print(resultFolder)

    for folderName, subFolder, filename in os.walk(inputFolder):

        for file in filename:

            if file.endswith(ext):

                filepath = os.path.join(os.path.abspath(folderName), file)

                if not os.path.exists(resultFolder):
                    #create result folder if it doesn't exist
                    os.makedirs(resultFolder)

                
                if os.path.dirname(filepath) != resultFolder:
                    #prevent copying files from result folder              
                    shutil.copy(filepath, resultFolder)
                    print(f'Copied {filepath} to result folder')


if __name__ == '__main__':
    selectiveCopy('.', 'png', 'result')