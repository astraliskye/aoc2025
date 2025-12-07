import unittest
import day7


class TestClass(unittest.TestCase):
    def test_example_solution_part1(self):
        result = day7.solve_part1()
        self.assertEqual(result, 21)

    def test_example_solution_part2(self):
        result = day7.solve_part2()
        self.assertEqual(result, 40)


if __name__ == '__main__':
    unittest.main()
