#! python3
# passwordBreaker.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 13 Project

import os


import PyPDF2


def breakPassword(filename):
    """Breaks a single word password of a PDF
    Args:
        filename (str): Filename for encrypted pdf
    Returns:
        None
    """
    encryptedFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(encryptedFile)

    with open('dictionary.txt') as words:
        wordList = words.read().split('\n')

    for word in wordList:
        wordLower = word.lower()
        wordCap = word.capitalize()

        if pdfReader.decrypt(word):
            return word
        elif pdfReader.decrypt(wordCap):
            return wordCap
        elif pdfReader.decrypt(wordLower):
            return wordLower

    return
        

if __name__ == "__main__":

    pdfWriter = PyPDF2.PdfFileWriter()
    pdfWriter.encrypt('ASPIRE')
    encryptedPdf = open('pdf_encrypted.pdf', 'wb')
    pdfWriter.write(encryptedPdf)
    encryptedPdf.close()

    print(breakPassword('pdf_encrypted.pdf'))

