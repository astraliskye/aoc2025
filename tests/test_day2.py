from ..day2.solver import (parse_input, get_invalid_ids, get_repeated_ids,
                           solve_part1, solve_part2)


def test_first_100():
    result = get_invalid_ids([(1, 100)])
    # .assertCountEqual tests that the two lists have the same items
    # regardless of order
    assert result == [11, 22, 33, 44, 55, 66, 77, 88, 99]


def test_part1_example_input():
    result = solve_part1(parse_input())
    assert result == 1227775554


def test_multi_digit():
    result = get_invalid_ids([(123100, 123200)])
    assert result == [123123]


def test_example_repeated_ids():
    result = get_repeated_ids(parse_input())
    assert result == [11, 22, 99, 111, 999, 1010, 1188511885,
                      222222, 446446, 38593859, 565656, 824824824,
                      2121212121]


def test_part2_example_input():
    result = solve_part2(parse_input())
    assert result == 4174379265
