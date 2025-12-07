def parse_input(example=True):
    filename = 'example_input.txt' if example else 'input.txt'
    lines = ''

    with open(filename) as file:
        lines = file.readlines()

    return lines


def solve_part1(example=True):
    input_lines = parse_input(example)
    beam_indices = set([input_lines[0].index('S')])
    splits = 0

    for line in input_lines[1:]:
        new_indices = []
        old_indices = []
        for beam in beam_indices:
            if line[beam] == '^':
                old_indices.append(beam)
                if beam > 0:
                    new_indices.append(beam - 1)
                if beam < len(line) - 1:
                    new_indices.append(beam + 1)
                splits += 1

        for new_index in new_indices:
            beam_indices.add(new_index)

        for old_index in old_indices:
            beam_indices.remove(old_index)

    return splits


def solve_part2(example=True):
    input = parse_input(example)
    pass


if __name__ == '__main__':
    print(f'Solution to part 1: {solve_part1(False)}')
    print(f'Solution to part 2: {solve_part2(False)}')
