# Bryant Perkins
# Introduction to Computer Programming
# Programming Assignment 3
# Due Date: 15 Nov 2020

import cipherMethods as Ciphers

fileName = input("What is the name of the message file? (include '.txt') ")
outputName = input("Name your output file: (include '.txt') ")
cipherChoice = input("Atbash, Caesar, or Qwerty cipher? (A, C, or Q) ")

# Atbashing message file
if cipherChoice.lower() == 'a':
    outputFile = open(outputName, 'w') if fileName != outputName else open('-' + outputName, 'w')
    with open(fileName) as messageFile:
        Ciphers.atbash_cipher(messageFile, outputFile)
# Qwerty message file
elif cipherChoice.lower() == 'q':
    enOrDe = input("Would you like to Encode or Decode a text file? (E or D) ")
    if not(enOrDe.lower() == 'e' or enOrDe.lower() == 'd'):
        print('Invalid input!')
        exit()
    outputFile = open(outputName, 'w') if fileName != outputName else open('-' + outputName, 'w')
    with open(fileName) as messageFile:
        Ciphers.qwerty_cipher(messageFile, outputFile, enOrDe)
# Caesar message file
elif cipherChoice.lower() == 'c':
    enOrDe = input("Would you like to Encode or Decode a text file? (E or D) ")
    shiftNum = input("What is the caesar shift magnitude? ")
    # Encoding caesar message file
    if enOrDe.lower() == 'e':
        outputFile = open(outputName, 'w')
        with open(fileName) as messageFile:
            Ciphers.encode_message(messageFile, outputFile, Ciphers.caesar_cipher(int(shiftNum)))
        outputFile.close()
    # Decoding caesar message file
    elif enOrDe.lower() == 'd':
        #   Decoding message file
        outputFile = open(outputName, 'w')
        with open(fileName) as messageFile:
            Ciphers.decode_message(messageFile, outputFile, Ciphers.caesar_cipher(int(shiftNum)*-1))
        outputFile.close()
    else:
        print('Invalid input!')
        exit()
# GOD MODE
elif cipherChoice.lower() == 'g':
    shiftNum = input("What is the caesar shift magnitude? ")
    outputFile = open(outputName, 'w') if fileName != outputName else open('-' + outputName, 'w')
    with open(fileName) as messageFile:
        Ciphers.qwerty_cipher(messageFile, outputFile, 'e')
        Ciphers.encode_message(messageFile, outputFile, Ciphers.caesar_cipher(int(shiftNum)))
        Ciphers.atbash_cipher(messageFile, outputFile)
        Ciphers.encode_message(messageFile, outputFile, Ciphers.caesar_cipher(int(shiftNum)))
        Ciphers.atbash_cipher(messageFile, outputFile)
        Ciphers.encode_message(messageFile, outputFile, Ciphers.caesar_cipher(int(shiftNum)))
        Ciphers.atbash_cipher(messageFile, outputFile)
        Ciphers.encode_message(messageFile, outputFile, Ciphers.caesar_cipher(int(shiftNum)))
    outputFile.close()
# All of the error handling
else:
    print('Invalid input!')
    exit()







