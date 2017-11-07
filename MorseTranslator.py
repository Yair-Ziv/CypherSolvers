"""
Morse translator tool
"""

LETTERS_TO_MORSE_DICT = {'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.',
                         'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..',
                         'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.',
                         's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-',
                         'y' : '-.--', 'z' : '--..', '1' : '.----', '2' : '..---', '3' : '...--',
                         '4' :  '....-', '5' : '.....', '6' : '-....', '7' : '--...', '8' : '---..',
                         '9' : '----.', '0' : '-----'}
MORSE_TO_LETTERS_DICT = {'.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e' , '..-.' : 'f',
                         '--.' : 'g', '....' : 'h', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l',
                         '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r',
                         '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x',
                         '-.--' : 'y', '--..' : 'z', '-----' : '0', '.----' : '1', '..---' : '2',
                         '...--' : '3', '....-' : '4', '.....' : '5', '-....' : '6', '--...' : '7',
                         '---..' : '8', '----.' : '9'}

def encode(to_encode):
    """
    Morse encoder
    """
    output = ''
    for letter in to_encode:
        try:
            output += LETTERS_TO_MORSE_DICT[letter] + '  '
        except KeyError:
            output += ''
    return output

def decode(to_decode):
    """
    Morse decoder
    """
    output = ''
    current_sequence = ''
    for letter in to_decode:
        if letter == ' ':
            try:
                output += MORSE_TO_LETTERS_DICT[current_sequence]
            except KeyError:
                print 'Sequence {} does not exist in the dictionary'.format(current_sequence)
            finally:
                current_sequence = ''
            continue
        current_sequence += letter
    try:
        output += MORSE_TO_LETTERS_DICT[current_sequence]
    except KeyError:
        print 'Sequence {} does not exist in the dictionary'.format(current_sequence)
    finally:
        current_sequence = ''
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


if __name__ == "__main__":
    main()
