# Bryant Perkins
# Introduction to Computer Programming
# Programming Assignment 3
# Due Date: 9 Nov 2020
import string


def qwerty_cipher(input_file, output_file, enOrDe):
    output = ''
    qwerty = "qwertyuiopasdfghjklzxcvbnm"
    if enOrDe.lower() == 'e':     # encoding
        qwertyDict = {string.ascii_letters[i]: qwerty[i] for i in range(len(qwerty))}
    else:   # decoding
        qwertyDict = {qwerty[i]: string.ascii_letters[i] for i in range(len(qwerty))}
    for letter in input_file.read().lower():
        output += qwertyDict[letter] if letter in string.ascii_lowercase else letter
    output_file.write(output)


def caesar_cipher(shift):
    # dictionary comprehension to create dictionary based on shift. % to eliminate full loops through alphabet
    return {i: string.ascii_lowercase[(i + shift) % 26] for i in range(len(string.ascii_lowercase))}


def decode_message(input_file, output_file, decoder):
    output = ''
    for letter in input_file.read().lower():
        # add decoded character one at a time to account for non-alphabetic characters [/n, " ", etc.]
        output += decoder[string.ascii_letters.index(letter)] if letter in string.ascii_lowercase else letter
    output_file.write(output)    # returned so the value can be passed into write function


# could have used a single function but you require both :)))
def encode_message(input_file, output_file, encoder):
    output = ''
    for letter in input_file.read().lower():
        output += encoder[string.ascii_letters.index(letter)] if letter in string.ascii_lowercase else letter
    output_file.write(output)


def atbash_cipher(input_file, output_file):
    output = ''
    cipher_dict = {string.ascii_lowercase[i]: string.ascii_lowercase[25-i] for i in range(len(string.ascii_lowercase))}
    for letter in input_file.read().lower():
        output += cipher_dict[letter] if letter in string.ascii_lowercase else letter
    output_file.write(output)
