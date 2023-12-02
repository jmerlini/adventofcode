import re
import number_dic
numberMap = number_dic.numbers


def parse_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines


def get_pattern():
    return '(?=(\d|' + '|'.join(numberMap.keys()) + '))'


def convert_words_to_numbers(digits):
    for i, digit in enumerate(digits):
        if(digit in numberMap.keys()):
            digits[i] = numberMap[digit]

    return digits


def retrieve_calibration_value(line, pattern):
    digits = re.findall(r'' + pattern, line)
    digits = convert_words_to_numbers(digits)

    return digits[0][0] + digits[-1][-1]


if __name__ == '__main__':
    lines = parse_file('input2.txt')
    values = []
    pattern = get_pattern()

    for line in lines:
        values.append(int(retrieve_calibration_value(line, pattern)))

    print(sum(values))