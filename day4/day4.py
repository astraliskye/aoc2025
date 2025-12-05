def parse_input(example=True):
    filename = 'example_input.txt' if example else 'input.txt'
    content = ''

    with open(filename) as file:
        content = file.readlines()

    output = []

    # Edit below to parse raw file text into usable data structures
    for line in content:
        output.append([True if x == '@' else False for x in line.strip()])

    return output


def get_neighbor_grid(grid):
    output = []
    for i, row in enumerate(grid):
        output.append([])
        for j, elem in enumerate(row):
            if not elem:
                output[i].append(-1)
                continue

            neighbors = 0

            if i > 0 and grid[i - 1][j]:
                neighbors += 1
            if i > 0 and j < len(row) - 1 and grid[i - 1][j + 1]:
                neighbors += 1
            if j < len(row) - 1 and grid[i][j + 1]:
                neighbors += 1
            if j < len(row) - 1 and i < len(grid) - 1 and grid[i + 1][j + 1]:
                neighbors += 1
            if i < len(grid) - 1 and grid[i + 1][j]:
                neighbors += 1
            if i < len(grid) - 1 and j > 0 and grid[i + 1][j - 1]:
                neighbors += 1
            if j > 0 and grid[i][j - 1]:
                neighbors += 1
            if i > 0 and j > 0 and grid[i - 1][j - 1]:
                neighbors += 1

            output[i].append(neighbors)

    return output


def remove_stacks(grid):
    n_removed = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < 0 or grid[i][j] >= 4:
                continue

            grid[i][j] = -1

            # Update neighbors
            if i > 0 and grid[i - 1][j] != -1:
                grid[i - 1][j] -= 1
            if i > 0 and j < len(grid[i]) - 1 and grid[i - 1][j + 1] != -1:
                grid[i - 1][j + 1] -= 1
            if j < len(grid[i]) - 1 and grid[i][j + 1]:
                grid[i][j + 1] -= 1
            if j < len(grid[i]) - 1 and i < len(grid) - 1 and grid[i + 1][j + 1] != -1:
                grid[i + 1][j + 1] -= 1
            if i < len(grid) - 1 and grid[i + 1][j] != -1:
                grid[i + 1][j] -= 1
            if i < len(grid) - 1 and j > 0 and grid[i + 1][j - 1] != -1:
                grid[i + 1][j - 1] -= 1
            if j > 0 and grid[i][j - 1] != -1:
                grid[i][j - 1] -= 1
            if i > 0 and j > 0 and grid[i - 1][j - 1] != -1:
                grid[i - 1][j - 1] -= 1

            n_removed += 1

    return n_removed


def solve_part1(example=True):
    grid = parse_input(example)
    neighbor_grid = get_neighbor_grid(grid)

    n_accessible = 0

    for row in neighbor_grid:
        n_accessible += sum([1 if x >= 0 and x < 4 else 0 for x in row])

    return n_accessible


def solve_part2(example=True):
    grid = parse_input(example)
    neighbor_grid = get_neighbor_grid(grid)

    total_removed = 0
    n_removed = 1
    while n_removed > 0:
        n_removed = remove_stacks(neighbor_grid)
        total_removed += n_removed

    return total_removed


if __name__ == '__main__':
    print(f'Solution to part 1: {solve_part1(False)}')
    print(f'Solution to part 2: {solve_part2(False)}')
