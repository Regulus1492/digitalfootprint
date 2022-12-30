
import argparse
import string

# Check for digits or special characters in strings

def no_digits_or_special_chars(string_in):
    if any(char.isdigit() for char in string_in):
        raise argparse.ArgumentTypeError('string contains digits')
    if any(char in string.punctuation for char in string_in):
        raise argparse.ArgumentTypeError('string contains special characters')
    return string_in