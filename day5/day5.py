def parse_input(example=True):
    filename = 'example_input.txt' if example else 'input.txt'
    lines = []

    with open(filename) as file:
        lines = file.readlines()

    # Edit below to parse raw file text into usable data structures
    ingred_ranges = []
    ingred_ids = []

    # Parse ranges
    line_index = 0
    line = lines[0].strip()
    while line != "":
        line_parts = line.strip().split("-")
        ingred_ranges.append((int(line_parts[0]), int(line_parts[1])))
        line_index += 1
        line = lines[line_index].strip()

    for line in lines[line_index + 1:]:
        ingred_ids.append(int(line.strip()))

    return ingred_ranges, ingred_ids


def solve_part1(example=True):
    ranges, ids = parse_input(example)

    fresh_map = []
    for id in ids:
        fresh = False
        for id_range in ranges:
            if id >= id_range[0] and id <= id_range[1]:
                fresh = True
                break
        fresh_map.append(int(fresh))

    return sum(fresh_map)


def do_ranges_overlap(range1, range2):
    crosses = (range1[0] <= range2[1] and range1[1] >= range2[1]) or (
        range2[0] <= range1[1] and range2[1] >= range1[1])
    contains = (range1[0] >= range2[0] and range1[1] <= range2[1]) or (
        range2[0] >= range1[0] and range2[1] <= range1[1])
    return crosses or contains


def merge_ranges(range1, range2):
    # Determine if they overlap
    if not do_ranges_overlap(range1, range2):
        return None, False

    return (min(range1[0], range2[0]), max(range1[1], range2[1])), True


def solve_part2(example=True):
    id_ranges, _ = parse_input(example)
    result_ranges = id_ranges.copy()

    # Merge all id ranges
    overlap = True
    while overlap and len(result_ranges) > 1:
        overlap = False
        for j in range(len(result_ranges) - 1):
            for i in range(j + 1, len(result_ranges)):
                merge, merged = merge_ranges(
                    result_ranges[j], result_ranges[i])

                if merged:
                    range1 = result_ranges[i]
                    range2 = result_ranges[j]
                    result_ranges.remove(range1)
                    result_ranges.remove(range2)
                    result_ranges.append(merge)
                    overlap = True
                    break

            if overlap:
                break

    # Sum size of all (now distinct) ranges
    return sum([r[1] + 1 - r[0] for r in result_ranges])


if __name__ == '__main__':
    print(f'Solution to part 1: {solve_part1(False)}')
    print(f'Solution to part 2: {solve_part2(False)}')
