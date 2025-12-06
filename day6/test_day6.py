import unittest
import day6


class TestClass(unittest.TestCase):
    def test_example_solution_part1(self):
        result = day6.solve_part1()
        self.assertEqual(result, 4277556)

    def test_example_solution_part2(self):
        result = day6.solve_part2()
        self.assertEqual(result, 3263827)


if __name__ == '__main__':
    unittest.main()
