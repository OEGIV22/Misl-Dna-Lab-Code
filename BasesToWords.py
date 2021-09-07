# -*- coding: utf-8 -*-
import numpy as np
def basestoWords(a):
    inputWord = a

    def split(inputWord):
        return[char for char in inputWord]
    letter_array = np.array(split(inputWord))

    n = 0 
    binary_storage = ''
    while n < len(letter_array):
        if (n % 4 == 0) and (n != 1) and (n!=0):
            binary_storage = binary_storage + ' '
        if letter_array[n] == "A":
            binary_storage = binary_storage + "00"
        elif letter_array[n] == "T":
            binary_storage = binary_storage + "01"
        elif letter_array[n] == "C":
            binary_storage = binary_storage + "10"
        elif letter_array[n] == "G":
            binary_storage = binary_storage + "11"
        else:
            binary_storage = binary_storage + "error"
        n = n+1
    binary_values = binary_storage.split()

    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    print(ascii_string)
