# -*- coding: utf-8 -*-
import numpy as np
# DNA Base to Bit
#A = "00"
#T = "01"
#C = "10"
#G = "11"

inputWord = input('Enter a word: ')

def split(inputWord):
    return[char for char in inputWord]
letter_array = np.array(split(inputWord))

binary_conversion = ''.join(format(ord(i), '08b') for i in inputWord)
i = 0
num = 0
binary_bases = [None]*int((len(binary_conversion)/2))
while i < len(binary_conversion):
    if i % 2 == 0:
         first = binary_conversion[i]
         second = binary_conversion[i+1]
         binary_bases[num] = first+second
         num = num + 1
    i = i + 1
n = 0
bases = [None]*int(len(binary_bases))
while n < len(binary_bases):
    if binary_bases[n] == "00":
        bases[n] = "A"
    elif binary_bases[n] == "01":
        bases[n] = "T"
    elif binary_bases[n] == "10":
        bases[n] = "C"
    elif binary_bases[n] == "11":
        bases[n] = "G"
    else:
        bases[n]= "error"
    n = n+1
final_string = ''.join(bases)
print(final_string)