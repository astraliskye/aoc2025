def parse_points(filename):
    lines = ''
    with open(filename) as file:
        lines = file.readlines()

    output = []
    for line in lines:
        line = line.strip()
        output.append(tuple([int(x) for x in line.split(',')]))

    return output


def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def contains_point(points, i, j):
    # Early exit for single-width rectangles
    if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
        return False

    # Order points by column
    if points[i][1] > points[j][1]:
        i, j = j, i

    # Whether the left-most coordinate is the bottom-left or top-left
    oriented_down = points[i][0] < points[j][0]

    # Look through all points
    for k in range(len(points)):
        # Skip the points we know are safe
        if k == i or k == j:
            continue

        if oriented_down:
            if points[k][0] > points[i][0] and points[k][0] < points[j][0] and points[k][1] > points[i][1] and points[k][1] < points[j][1]:
                return True
        else:
            if points[k][0] < points[i][0] and points[k][0] > points[j][0] and points[k][1] > points[i][1] and points[k][1] < points[j][1]:
                return True

    return False


def largest_area_at_index(points, i):
    max_area = 0
    point = points[i]

    # Look forward
    for k in range(len(points) - 1):
        current_index = (i + k) % len(points)
        if contains_point(points, i, current_index):
            break

        other_point = points[current_index]
        max_area = max(max_area, area(point, other_point))

    # Look Backward
    for k in range(len(points) - 1):
        current_index = (i - k) % len(points)
        if contains_point(points, i, current_index):
            break

        other_point = points[current_index]
        max_area = max(max_area, area(point, other_point))

    return max_area


def solve_part1(example=True):
    filename = 'day9/example_input.txt' if example else 'day9/input.txt'
    points = parse_points(filename)

    max_area = 0

    for i in range(len(points) - 1):
        for j in range(1, len(points)):
            max_area = max(max_area, area(points[i], points[j]))

    return max_area


def solve_part2(example=True):
    filename = 'day9/example_input.txt' if example else 'day9/input.txt'
    points = parse_points(filename)

    max_area = 0

    for i in range(len(points)):
        max_area = max(max_area, largest_area_at_index(points, i))

    return max_area


if __name__ == '__main__':
    print(f'Solution to part 1: {solve_part1(False)}')
    print(f'Solution to part 2: {solve_part2(False)}')
