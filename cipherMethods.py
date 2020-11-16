# Bryant Perkins
# Introduction to Computer Programming
# Programming Assignment 3
# Due Date: 9 Nov 2020
import string


def caesar_cipher(shift):
    return {i: string.ascii_lowercase[(i + shift) % 26] for i in range(len(string.ascii_lowercase))}


def decode_message(input_file, output_file, decoder):
    content = input_file.read().lower()
    output = ''
    for letter in content:
        output += decoder[string.ascii_letters.index(letter)] if letter in string.ascii_lowercase else " "
    return output_file.write(output)


def encode_message(input_file, output_file, encoder):
    content = input_file.read().lower()
    output = ''
    for letter in content:
        output += encoder[string.ascii_letters.index(letter)] if letter in string.ascii_lowercase else " "
    return output_file.write(output)


if __name__ == "__main__":
    outputFile = open("outputHere.txt", 'w')
    with open("encoded_text.txt") as workingFile:
        encode_message(workingFile, outputFile, caesar_cipher(5))
        outputFile = open("outputHere.txt", 'r')
        print(outputFile.read())
else:
    print("coolcool")
