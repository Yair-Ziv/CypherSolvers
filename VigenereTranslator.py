"""
Solves Vignere Cypher
"""
from CaesarTranslator import convert
import GematriaTranslator as gt


NUM_LETTERS_ABC = ord('z') - ord('a')

def key_skips(keys_string):
    """
    Returns a list containing the gematric values of each letter in the key
    """
    keys_array = []
    for letter in keys_string:
        keys_array.append(int(gt.encode(letter).strip()))
    return keys_array

def encode(string_to_encode, cypher_key):
    """
    Encodes a Vigenere Cypher
    """
    cypher_key_gematric = key_skips(cypher_key)

    output = ''

    counter = 0
    for letter in string_to_encode:
        new_letter = convert(letter, cypher_key_gematric[counter] - 1)
        output += new_letter

        counter = (counter + 1) % len(cypher_key)

    return output


def decode(string_to_decode, cypher_key):
    """
    Decodes a Vigenere Cypher
    TODO Finish the decoder, rememeber that -key = 24 - key
    """
    cypher_key_gematric = key_skips(cypher_key)

    output = ''

    counter = 0
    for letter in string_to_decode:
        new_letter = convert(letter, NUM_LETTERS_ABC - cypher_key_gematric[counter] + 2)
        output += new_letter

        counter = (counter + 1) % len(cypher_key)

    return output

def main():
    """
    Main function
    """
    answer_type = raw_input('Would you like to encode or decode?\n').lower()
    while True:
        if answer_type == 'encode' or answer_type == 'decode':
            break
        else:
            print '\n\nAnswer only encode or decode'
        answer_type = raw_input('Would you like to encode or decode?\n').lower()

    if answer_type == 'encode':
        print encode(raw_input('\nWhat would you like to encode?\n'),
                     raw_input('\nWhat is the cypher key?\n'))
    elif answer_type == 'decode':
        print decode(raw_input('\nWhat would you like to decode?\n'),
                     raw_input('\nWhat is the cypher key?\n'))

if __name__ == '__main__':
    main()
