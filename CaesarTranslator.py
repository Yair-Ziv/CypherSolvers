"""
Encodes and decodes caesar
"""
import string

def exists_in_string(letter, string):
    """
    Checks if a letter exists in a string
    """
    for _letter in string:
        if letter == _letter:
            return True
    return False

def convert(string_to_convert, skip_value):
    """
    Converts a string to skip_value steps forward\n
    skip_value -- Amount to skip
    """
    string_to_convert = string_to_convert.lower()
    new_string = ''
    for letter in string_to_convert:
        if exists_in_string(letter, string.letters):
            current_value = ord(letter)
            if not current_value + skip_value > ord('z'):
                current_value += skip_value
            else:
                current_value = ord('a') + (current_value + skip_value) - ord('z') - 1
            new_string += chr(current_value)
        else:
            new_string += letter

    return new_string

def main():
    """
    Main function
    """
    string_to_convert = raw_input('What string would you like to convert?\n')
    try:
        skip_value = int(raw_input('\nHow much would you like to skip?\n'))
        convert(string_to_convert, skip_value)
    except ValueError:
        print 'This is not a number'
        main()

if __name__ == '__main__':
    main()

