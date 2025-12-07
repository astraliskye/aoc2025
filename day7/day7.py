def parse_input(example=True):
    filename = 'example_input.txt' if example else 'input.txt'
    content = ''

    with open(filename) as file:
        content = file.read()

    # Edit below to parse raw file text into usable data structures
    output = content

    return output


def solve_part1(example=True):
    input = parse_input(example)
    pass


def solve_part2(example=True):
    input = parse_input(example)
    pass


if __name__ == '__main__':
    print(f'Solution to part 1: {solve_part1(False)}')
    print(f'Solution to part 2: {solve_part2(False)}')
