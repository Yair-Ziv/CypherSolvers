"""
Encodes and decodes binary
"""

def translate_sequence(sequence):
    """
    Translates a binary sequence into a char
    """
    binary_sum = 0
    sequence_length = len(sequence)
    for i in range(sequence_length):
        if sequence[i] == '1':
            binary_sum += 2 ** (sequence_length - (i + 1))
    return chr(binary_sum)

def encode(to_encode):
    """
    Encodes strings to binary
    """
    output = ''
    for letter in to_encode:
        letter_value = ord(letter)
        letter_binary = ''
        if not letter == ' ':
            for i in range(7, -1, -1):
                if letter_value - 2 ** i >= 0:
                    letter_binary += '1'
                    letter_value -= 2 ** i
                else:
                    letter_binary += '0'
            output += letter_binary + ' '
        else:
            output += ' '
    return output

def decode(to_decode):
    """
    Decodes binary to string
    """
    output = ''
    current_sequence = ''
    for letter in to_decode:
        if letter == ' ':
            output += translate_sequence(current_sequence)
            current_sequence = ''
        else:
            current_sequence += letter
    output += translate_sequence(current_sequence)

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
