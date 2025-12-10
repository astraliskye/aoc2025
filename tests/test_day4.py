from ..day4.solver import (parse_input, solve_part1, solve_part2)


def test_example_solution_part1():
    result = solve_part1(parse_input())
    assert result == 13


def test_example_solution_part2():
    result = solve_part2(parse_input())
    assert result == 43
