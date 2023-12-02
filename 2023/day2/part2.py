import re

colors = [
    'red',
    'green',
    'blue'
]


def parse_file(file):
    with open(file) as f:
        lines = f.readlines()
    return lines


def find_power_of_game(game):
    power = 1
    for color in colors:
        pattern = '(\d+) ' + color
        power *= max([int(x) for x in re.findall(r'' + pattern, game)])
    return power


def find_total_power_of_games(games):
    total_power = 0
    for game in games:
        total_power += find_power_of_game(game)
    return total_power


if __name__ == '__main__':
    games = parse_file('input2.txt')
    print(find_total_power_of_games(games))
