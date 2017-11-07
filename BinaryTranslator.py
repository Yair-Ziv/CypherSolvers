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

def encode():
    """
    Encodes strings to binary
    """
    user_input = raw_input('What would you like to encode?\n')
    output = ''
    for letter in user_input:
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
    print output

def decode():
    """
    Decodes binary to string
    """
    user_input = raw_input('What would you like to decode?\n')
    output = ''
    current_sequence = ''
    for letter in user_input: <>
        if letter == ' ':
            output += translate_sequence(current_sequence)
            current_sequence = ''
        else:
            current_sequence += letter
    output += translate_sequence(current_sequence)

    print 'Output: {}'.format(output)

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
