
# Jonathan Masino    6/8/2021    Assignment 3: Cryptography App Using Files    Dr. Marques

import string
alphabets = [string.ascii_uppercase, string.ascii_lowercase]
key = 3

print("\nWelcome, this assignment is an extension of Assignment 2.")
print("Here, we will read words from a text file and the user will choose to either encrypt or decrypt.")
print("The encrypted or decrypted word is then printed to another text file. \n")

def encrypt(word, key):
    def enc_shift_alph(alphabets):
        return alphabets[int(key):] + alphabets[:int(key)] 
    enc_shifted = tuple(map(enc_shift_alph, alphabets))
    enc_new_alphabet = ''.join(alphabets)
    enc_shifted_alphabet = ''.join(enc_shifted)
    enc_table = str.maketrans(enc_new_alphabet, enc_shifted_alphabet)
    encrypted = word.translate(enc_table)
    return encrypted

def decrypt(word, key):
    def dec_shift_alph(alphabets):
            return alphabets[(-1 * int(key)):] + alphabets[:(-1 * int(key))]
    dec_shifted = tuple(map(dec_shift_alph, alphabets))
    dec_new_alphabet = ''.join(alphabets)
    dec_shifted_alphabet = ''.join(dec_shifted)
    dec_table = str.maketrans(dec_new_alphabet, dec_shifted_alphabet)
    decrypted = word.translate(dec_table)
    return decrypted

playAgain_str = "y"
while playAgain_str == 'y':
    input_filename = input('Please enter the file name you would like to pull a word from: ')
    enc_or_dec = input('Would you like to encrypt or decrypt? (e or d): ')

    if enc_or_dec == "e":
        enc_in_file = open (input_filename, "r")
        word_enc = enc_in_file.readline()
        output_filename_enc = ""
        i = 0
        while input_filename[i] != '.':
            output_filename_enc += input_filename[i]
            i = i + 1
        output_filename_enc += '_enc.txt'
        enc_out_file = open(output_filename_enc, 'w')
        enc_out_file.write(encrypt(word_enc, key))
        print("Your encrypted word has printed to " + output_filename_enc)
        enc_in_file.close()
        enc_out_file.close()

    elif enc_or_dec == "d":
        dec_in_file = open (input_filename, "r")
        word_dec = dec_in_file.readline()
        output_filename_dec = ""
        j = 0
        while input_filename[j] != '.':
            output_filename_dec += input_filename[j]
            j = j + 1
        output_filename_dec += '_dec.txt'
        dec_out_file = open(output_filename_dec, 'w')
        dec_out_file.write(decrypt(word_dec, key))
        print("Your decrypted word has printed to " + output_filename_dec)
        dec_in_file.close()
        dec_out_file.close()

    else:
        print("Invalid entry. Please enter either e or d")

    playAgain_str = input('Would you like to play again? (y or n): ')
    if playAgain_str != 'y':
        print("Have a good day!")