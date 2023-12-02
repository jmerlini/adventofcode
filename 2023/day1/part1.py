import re


def parse_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines


def retrieve_calibration_value(line):
    digits = re.findall(r'\d', line)
    return digits[0] + digits[-1]


if __name__ == '__main__':
    lines = parse_file('input2.txt')
    values = []

    for line in lines:
        values.append(int(retrieve_calibration_value(line)))

    print(sum(values))
