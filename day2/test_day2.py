import unittest
from day2 import (parse_input, get_invalid_ids, get_repeated_ids,
                  solve_part1, solve_part2)


class TestClass(unittest.TestCase):  # Test cases for my sanity
    def test_first_100(self):
        result = get_invalid_ids([(1, 100)])
        # .assertCountEqual tests that the two lists have the same items
        # regardless of order
        self.assertCountEqual(result, [22, 11, 33, 44, 55, 66, 77, 88, 99],
                              'Could not select all IDs less than 100')

    def test_part1_example_input(self):
        result = solve_part1(parse_input())
        self.assertEqual(result, 1227775554, 'Wrong example solution part 1')

    def test_multi_digit(self):
        result = get_invalid_ids([(123100, 123200)])
        self.assertIn(123123, result, 'Could not select invalid IDs with'
                      + 'multi-digit repetitions')

    def test_example_repeated_ids(self):
        result = get_repeated_ids(parse_input())
        self.assertCountEqual(result, [11, 22, 99, 111, 999, 1010, 1188511885,
                              222222, 446446, 38593859, 565656, 824824824,
                                       2121212121])

    def test_part2_example_input(self):
        result = solve_part2(parse_input())
        self.assertEqual(result, 4174379265, 'Wrong example solution part 2')


if __name__ == '__main__':
    unittest.main()
