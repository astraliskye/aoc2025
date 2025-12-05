import unittest
import day4


class TestClass(unittest.TestCase):
    def test_example_solution_part1(self):
        result = day4.solve_part1(day4.parse_input())
        self.assertEqual(result, 13)

    def test_example_solution_part2(self):
        result = day4.solve_part2(day4.parse_input())
        self.assertEqual(result, 43)


if __name__ == '__main__':
    unittest.main()
