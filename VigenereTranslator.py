"""
Solves Vignere Cypher
"""
from CaesarTranslator import convert
from GimatryTranslator import decode

def key_skips(keys_string):
    keys_array = []
    for letter in keys_string:
        new_value = ord(letter) - ord('a') + 1
        keys_array.append(new_value)

def encode():
    """
    Encodes a Vigenere Cypher
    TODO Finish the encoder
    """
    string_to_encode = raw_input('\nWhat would you like to encode?\n')
    cypher_key = raw_input('\nWhat is the cypher key?\n')

    output = ''
    # for i in range(len(string_to_encode)):
    print key_skips(cypher_key)

def decode():
    """
    Decodes a Vigenere Cypher
    TODO Finish the decoder, rememeber that -key = 24 - key
    """
    pass

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
        encode()
    elif answer_type == 'decode':
        decode()

if __name__ == '__main__':
    main()