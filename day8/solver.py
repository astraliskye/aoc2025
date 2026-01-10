import math
import sys


def parse_input(example):
    filename = 'day8/example_input.txt' if example else 'day8/input.txt'
    lines = ''
    with open(filename) as file:
        lines = file.readlines()

    output = []
    for line in lines:
        line = line.strip()
        output.append(tuple([int(x) for x in line.split(',')]))

    return output


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 +
                     (a[1] - b[1]) ** 2 +
                     (a[2] - b[2]) ** 2)


def closest_two_points(points):
    if len(points) < 2:
        return (-1, -1)
    elif len(points) == 2:
        return (0, 1)
    min_distance = sys.maxsize
    min_dist_indices = (-1, -1)

    for i in range(len(points) - 1):
        for j in range(1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                min_dist_indices = (i, j)

    return min_dist_indices


def solve_part1(example=True):
    points = set(parse_input(example))
    n = 10 if example else 1000
    circuits = []
    point_circuits = {}

    for i in range(n):
        pass

    return points


def solve_part2(example=True):
    pass


if __name__ == '__main__':
    print(f'Solution to part 1: {solve_part1(False)}')
    print(f'Solution to part 2: {solve_part2(False)}')
