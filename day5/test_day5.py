import unittest
import day5


class TestClass(unittest.TestCase):
    def test_example_solution_part1(self):
        result = day5.solve_part1()
        self.assertEqual(result, 3)

    def test_example_solution_part2(self):
        result = day5.solve_part2()
        self.assertEqual(result, 14)


if __name__ == "__main__":
    unittest.main()
