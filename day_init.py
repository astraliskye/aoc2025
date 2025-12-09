import requests
import os
from dotenv import load_dotenv
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Advent of Code Day Initializer',
        description='Takes care of the AoC daily boilerplate'
    )

    parser.add_argument('day')
    parser.add_argument('-g', '--getinput', action='store_true')
    parser.add_argument('-t', '--tests', action='store_true')

    args = parser.parse_args()

    day = int(args.day)

    print(f'Creating file')

    script_content = '''def solve_part1(example=True):
    pass


def solve_part2(example=True):
    pass


if __name__ == '__main__':
    print(f'Solution to part 1: {solve_part1(False)}')
    print(f'Solution to part 2: {solve_part2(False)}')'''

    print(f'Creating file: day{day}/solver.py')

    dirpath = os.path.join(os.getcwd(), 'day8')

    if not os.path.exists(dirpath):
        os.makedirs(f'./day{day}')

    with open(f'./day{day}/solver.py', 'w+') as file:
        file.write(script_content)

    if args.tests:
        print(f'Creating test file: tests/test_day{day}.py')
        test_content = f'''from ..day{day}.solver import solve_part1, solve_part2

def test_solution_part_1():
    result = solve_part1()
    assert 1 == 0


def test_solution_part_2():
    result = solve_part2()
    assert 1 == 0'''

        with open(f'./tests/test_day{day}.py', 'w+') as file:
            file.write(test_content)

    if args.getinput:
        print(f'Retrieving input: day{day}/input.txt')
        load_dotenv()

        INPUT_URL = f'https://adventofcode.com/2025/day/{day}/input'
        input = requests.get(
            INPUT_URL, headers={'Cookie': f'session={os.getenv('SESSION_COOKIE')}'})

        with open(f'./day{day}/input.txt', 'w+') as file:
            file.write(input.text)
