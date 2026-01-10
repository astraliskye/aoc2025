import sys
import math
from functools import reduce
from itertools import islice
import operator


def parse_points(filename):
    lines = []
    with open(filename) as file:
        lines = file.readlines()

    output = []
    for line in lines:
        line = line.strip()
        output.append(tuple([int(x) for x in line.split(",")]))

    return output


def product(ns):
    return reduce(operator.mul, ns, 1)


def distance3d(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def find_closest_points(points, circuits):
    min_dist = sys.maxsize
    min_indices = (-1, -1)

    for i in range(len(points) - 1):
        for j in range(1, len(points)):
            same_circuit = False
            for c in circuits:
                if i in c and j in c:
                    same_circuit = True

            dist = distance3d(points[i], points[j])
            if dist < min_dist and not same_circuit:
                dist = min_dist
                min_indices = (i, j)

    return min_indices


def solve_part1(example=True):
    filename = "day8/example_input.txt" if example else "day8/input.txt"
    points = parse_points(filename)

    iterations = 10 if example else 1000
    circuits = [[i] for i in range(len(points))]

    for _ in range(iterations):
        a, b = find_closest_points(points, circuits)

        c_index_a = -1
        c_index_b = -1

        for i in range(len(circuits)):
            if a in circuits[i]:
                c_index_a = i
            if b in circuits[i]:
                c_index_b = i

        new_circuits = []
        for i in range(len(circuits)):
            if i == c_index_a or i == c_index_b:
                continue
            new_circuits.append(circuits[i])

        c_a = circuits[c_index_a]
        c_b = circuits[c_index_b]
        new_circuits.append(c_a + c_b)
        circuits = new_circuits

    print(circuits)
    print(len(circuits))

    return product(islice(reversed(sorted([len(c) for c in circuits])), 5))


def solve_part2(example=True):
    pass


if __name__ == "__main__":
    print(f"Solution to part 1: {solve_part1(False)}")
    print(f"Solution to part 2: {solve_part2(False)}")
