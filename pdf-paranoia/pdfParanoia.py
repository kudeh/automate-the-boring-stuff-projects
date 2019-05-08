#! python3
# pdfParanoia.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 13 Project

import os


import PyPDF2


def encryptPDFs(root, password):
    """Encrypts all pdfs folder walk
       Args:
          root (str): folder path to walk
       Returns:
          None
    """
    for folder, subfolder, fileList in os.walk(root):
        for file in fileList:
            if file.endswith('.pdf'):
                filepath = os.path.join(os.path.abspath(folder), file)
                pdfFileObj = open(filepath, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                pdfWriter = PyPDF2.PdfFileWriter()

                if not pdfReader.isEncrypted:
                    pdfWriter.encrypt(password)
                    newPath = os.path.dirname(filepath) + '/' + \
                              ('_encrypted.'.join(os.path.basename(filepath).split('.')))
                    resultPdf = open(newPath, 'wb')
                    pdfWriter.write(resultPdf)
                    resultPdf.close()


if __name__ == "__main__":

    password = input('Enter encryption password: ')
    encryptPDFs('/Users/keneudeh/Downloads/automate_online-materials', password)