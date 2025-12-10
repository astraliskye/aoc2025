from ..day3.solver import (parse_input, solve_part1,
                           solve_part2, get_joltage_from_row)


def test_joltages_part1():
    rows = parse_input()
    joltages = []

    for row in rows:
        joltages.append(get_joltage_from_row(row, 2))

    assert len(joltages) == 4
    assert joltages == [98, 89, 78, 92]


def test_joltages_part2():
    rows = parse_input()
    joltages = []

    for row in rows:
        joltages.append(get_joltage_from_row(row, 12))

    assert len(joltages) == 4
    assert joltages == [987654321111,
                        811111111119, 434234234278, 888911112111]


def test_example_solution_part1():
    result = solve_part1()
    assert result == 357


def test_example_solution_part2():
    result = solve_part2()
    assert result == 3121910778619
