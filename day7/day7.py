def parse_input(example=True):
    filename = 'example_input.txt' if example else 'input.txt'
    lines = ''

    with open(filename) as file:
        lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

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
    input_lines = parse_input(example)
    beam_indices = {}
    for i in range(len(input_lines[0])):
        beam_indices[i] = 0

    beam_indices[input_lines[0].index('S')] = 1
    timelines = 1

    for line in input_lines[1:]:
        for beam, amount in beam_indices.copy().items():
            if line[beam] == '^' and amount != 0:
                beam_indices[beam] = 0

                if (beam - 1) in beam_indices:
                    beam_indices[beam - 1] += amount
                else:
                    beam_indices[beam - 1] = amount

                if (beam + 1) in beam_indices:
                    beam_indices[beam + 1] += amount
                else:
                    beam_indices[beam + 1] = amount

                timelines += amount

    return timelines


if __name__ == '__main__':
    print(f'Solution to part 1: {solve_part1(False)}')
    print(f'Solution to part 2: {solve_part2(False)}')
