import re

total_balls = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def parse_file(file):
    with open(file) as f:
        lines = f.readlines()

    return lines


def is_game_valid(game):
    for color in total_balls.keys():
        pattern = '(\d+) ' + color
        if max([int(x) for x in re.findall(r'' + pattern, game)]) > total_balls[color]:
            return False

    return True


def find_total_of_valid_games(games):
    total_of_valid_games = 0
    for game in games:
        if is_game_valid(game):
            game_id = re.findall(r'Game (\d+):', game)[0]
            total_of_valid_games += int(game_id)
    return total_of_valid_games


if __name__ == '__main__':
    games = parse_file('input2.txt')
    print(find_total_of_valid_games(games))
