def readfile(filepath):
    input_file = open(filepath, 'r')
    input = input_file.read()
    input_file.close()
    return input


# Despite the type annotation, nothing complains if the return value
# is not [(int, int)]
def parse_input(example=True) -> [(int, int)]:
    content = ''

    if example:
        content = readfile('day2/example_input.txt')
    else:
        content = readfile('day2/input.txt')

    raw_ranges = content.split(',')
    # Prefer to use comprehensions over map(), it's just cleaner
    ranges = [(int(y[0]), int(y[1])) for y in
              [x.split('-') for x in raw_ranges]]

    return ranges


def get_invalid_ids(id_ranges_list):
    invalid_ids = []

    for id_range in id_ranges_list:
        for i in range(id_range[0], id_range[1] + 1):
            id_string = str(i)
            half_index = len(id_string) // 2
            if id_string[:half_index] == id_string[half_index:]:
                invalid_ids.append(int(i))

    return invalid_ids


def partition_string(string, n):
    partitions = []
    for i in range(0, len(string), n):
        partitions.append(string[i:i+n])
    return partitions


def get_repeated_ids(id_ranges_list):
    repeated_ids = []

    for id_range in id_ranges_list:
        for i in range(id_range[0], id_range[1] + 1):
            id_string = str(i)
            for j in range(1, len(id_string) // 2 + 1):
                partitions = partition_string(id_string, j)
                if all([p == partitions[0] for p in partitions]):
                    repeated_ids.append(i)
                    break

    return repeated_ids


def solve_part1(example=True):
    ranges = parse_input(example)
    return sum(get_invalid_ids(ranges))


def solve_part2(example=True):
    ranges = parse_input(example)
    return sum(get_repeated_ids(ranges))


if __name__ == '__main__':
    print(f'Part 1 solution: {solve_part1(parse_input(False))}')
    print(f'Part 2 solution: {solve_part2(parse_input(False))}')
