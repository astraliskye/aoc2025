from ..day7.solver import solve_part1, solve_part2


def test_example_solution_part1():
    result = solve_part1()
    assert result == 21


def test_example_solution_part2():
    result = solve_part2()
    assert result == 40
