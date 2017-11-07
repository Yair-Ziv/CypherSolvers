"""
Encodes and decodes gimatry
"""

def encode(to_encode):
    """
    Encodes the user input to a gimatry
    """
    output = ''
    for letter in to_encode:
        output += '{} '.format(ord(letter) - ord('a') + 1)
    return output

def decode(to_decode):
    """
    Decodes a gimatry sequence to a string
    """
    output = ''
    current_sequence = 0
    for letter in to_decode:
        if not letter == ' ':
            current_sequence *= 10
            try:
                current_sequence += int(letter)
            except ValueError:
                continue
        else:
            output += chr(current_sequence + ord('a') - 1)
            current_sequence = 0
    output += chr(current_sequence + ord('a') - 1)
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
        print encode(raw_input('\nWhat would you like to encode?\n'))
    elif answer_type == 'decode':
        print decode(raw_input('\nWhat would you like to decode?\n'))

if __name__ == '__main__':
    main()