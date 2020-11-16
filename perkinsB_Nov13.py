# Bryant Perkins
# Introduction to Computer Programming
# Programming Assignment 2
# Due Date: 13 Nov 2020

import string

userMessage = input("What is your secret message? ")


def atbash_cipher(message):
    message = message.lower()
    final_cipher = ""
    cipher_dict = {string.ascii_lowercase[i]: string.ascii_lowercase[25-i] for i in range(len(string.ascii_lowercase))}
    for letter in message:
        final_cipher += cipher_dict[letter] if letter in string.ascii_lowercase else " "
    print("Atbashed:", final_cipher)


atbash_cipher(userMessage)
