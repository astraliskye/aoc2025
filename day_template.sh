#!/bin/zsh

main_content="def parse_input(example=True):
    filename = 'example_input.txt' if example else 'input.txt'
    content = ''

    with open(filename) as file:
        content = file.read()

    # Edit below to parse raw file text into usable data structures
    output = content

    return output


def solve_part1(example=True):
    input = parse_input(example)
    pass


def solve_part2(example=True):
    input = parse_input(example)
    pass


if __name__ == '__main__':
    print(f'Solution to part 1: {solve_part1(False)}')
    print(f'Solution to part 2: {solve_part2(False)}')"

test_content="import unittest
import day${1}


class TestClass(unittest.TestCase):
    def test_intermediate_part1(self):
        pass

    def test_intermediate_part2(self):
        pass

    def test_example_solution_part1(self):
        pass

    def test_example_solution_part2(self):
        pass


if __name__ == "__main__":
    unittest.main()"

mkdir "day${1}"
echo $main_content >"day${1}/day${1}.py"
echo $test_content >"day${1}/test_day${1}.py"
