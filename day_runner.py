import argparse
import importlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'AoC Solution Runner',
        'Runs AoC solutions with official input'
    )

    parser.add_argument('-e', '--example', action='store_true')
    parser.add_argument('-d', '--days', action='extend', nargs='+')

    args = parser.parse_args()

    for day in args.days:
        day = int(day)

        module = importlib.import_module(f'day{day}.solver')
        part1 = getattr(module, 'solve_part1')
        part2 = getattr(module, 'solve_part2')

        print(f'Day {day} part 1: {part1(args.example)}')
        print(f'Day {day} part 2: {part2(args.example)}')
