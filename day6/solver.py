def parse_input(example=True):
    filename = 'day6/example_input.txt' if example else 'day6/input.txt'
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


def parse_input_part2(example=True):
    filename = 'day6/example_input.txt' if example else 'day6/input.txt'
    lines = ''

    with open(filename) as file:
        lines = file.readlines()

    lines = list(zip(*lines))
    problems = []
    problems.append([lines[0][-1]])  # Start the first problem
    for i, line in enumerate(lines):
        if all([x == "\n" or x == "\r\n" for x in line]):
            break

        if all([x == " " for x in line]):
            problems.append([lines[i + 1][-1]])
            continue

        problems[-1].append(int(''.join(filter(lambda x: x !=
                            " ", line[:-1]))))

    return problems


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
    problems = parse_input_part2(example)

    result = 0

    for problem in problems:
        if problem[0] == "+":
            result += sum(problem[1:])
        else:
            result += product(problem[1:])

    return result


if __name__ == '__main__':
    print(f'Solution to part 1: {solve_part1(False)}')
    print(f'Solution to part 2: {solve_part2(False)}')
