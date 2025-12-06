def parse_input(example=True):
    filename = 'example_input.txt' if example else 'input.txt'
    lines = ''

    with open(filename) as file:
        lines = file.readlines()

    lines = [line.strip().split() for line in lines]

    output = list(zip(*lines))
    for i in range(len(output)):
        output[i] = list(output[i])
        for j in range(len(output[i]) - 1):
            output[i][j] = int(output[i][j])

    return output


def product(ns):
    if len(ns) <= 0:
        return 0

    result = ns[0]

    for n in ns[1:]:
        result *= n

    return result


def solve_part1(example=True):
    problems = parse_input(example)

    result = 0

    for problem in problems:
        if problem[-1] == "+":
            result += sum(problem[:-1])
        else:
            result += product(problem[:-1])

    return result


def solve_part2(example=True):
    input = parse_input(example)
    pass


if __name__ == '__main__':
    print(f'Solution to part 1: {solve_part1(False)}')
    print(f'Solution to part 2: {solve_part2(False)}')
