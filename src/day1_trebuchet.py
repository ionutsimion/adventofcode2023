import re


def extract_digits(line):
    digits_as_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    pattern = re.compile(fr'{"|".join(map(re.escape, digits_as_words))}|\d')
    return pattern.findall(line)


def replace_literals_with_digits(literal_digits):
    literals_to_digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                          'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    return [literal_digit if literal_digit.isdigit() else literals_to_digits[literal_digit]
            for literal_digit in literal_digits]


def make_number_with_first_and_last_digit(digits):
    return int(digits[0]) * 10 + int(digits[-1])


with open('../data/day1_input.txt') as f:
    print(sum([make_number_with_first_and_last_digit(replace_literals_with_digits(extract_digits(line)))
               for line in f.readlines()]))
