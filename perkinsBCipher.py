# Bryant Perkins
# Introduction to Computer Programming
# Programming Assignment 3
# Due Date: 15 Nov 2020

import cipherMethods as Ciphers

enOrDe = input("Would you like to Encode or Decode a text file? (E or D) ")
fileName = input("What is the name of this file? (include '.txt') ")
shiftNum = int(input("What is the caesar shift magnitude? "))

if enOrDe.lower() == 'e':
    #   Encoding message file
    outputFile = open("outputHere.txt", 'w')
    with open(fileName) as messageFile:
        Ciphers.encode_message(messageFile, outputFile, Ciphers.caesar_cipher(shiftNum))
    print(outputFile.read())
elif enOrDe.lower() == 'd':
    #   Decoding message file
    messageFile = open("outputHere.txt", 'r')
    print(messageFile.read())
    with open(fileName) as workingFile:
        Ciphers.decode_message(workingFile, messageFile, Ciphers.caesar_cipher(shiftNum * -1))
else:
    print('Invalid input!')
    exit()






