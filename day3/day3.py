def parse_input(example=True):
    filename = 'example_input.txt' if example else 'input.txt'
    content = ''

    with open(filename) as file:
        content = file.readlines()

    output = [list(map(int, row.strip())) for row in content]

    return output


def solve_part1(example=True):
    input = parse_input(example)

    sum = 0

    for row in input:
        sum += get_joltage_from_row(row, 2)

    return sum


def get_joltage_from_row(row, n):
    max_digits = []
    current_start = 0

    for i in range(n):
        max = 0
        max_index = -1
        for j, elem in enumerate(row[current_start:len(row) - (n - i - 1)]):
            if elem > max:
                max = elem
                max_index = current_start + j
        current_start = max_index + 1
        max_digits.append(max)

    result = 0
    for i, elem in enumerate(max_digits):
        result += elem * (10 ** (len(max_digits) - i - 1))

    return result


def solve_part2(example=True):
    input = parse_input(example)

    sum = 0

    for row in input:
        sum += get_joltage_from_row(row, 12)

    return sum


if __name__ == '__main__':
    print(f'Solution to part 1: {solve_part1(False)}')
    print(f'Solution to part 2: {solve_part2(False)}')
