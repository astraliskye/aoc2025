import unittest
import day3


class TestClass(unittest.TestCase):
    def test_joltages_part1(self):
        rows = day3.parse_input()
        joltages = []

        for row in rows:
            joltages.append(day3.get_joltage_from_row(row, 2))

        self.assertEqual(len(joltages), 4, 'Wrong number of joltages returned')
        self.assertCountEqual(joltages, [98, 89, 78, 92])

    def test_joltages_part2(self):
        rows = day3.parse_input()
        joltages = []

        for row in rows:
            joltages.append(day3.get_joltage_from_row(row, 12))

        self.assertEqual(len(joltages), 4, 'Wrong number of joltages returned')
        self.assertCountEqual(joltages, [987654321111,
                              811111111119, 434234234278, 888911112111])

    def test_example_solution_part1(self):
        result = day3.solve_part1()
        self.assertEqual(result, 357, 'Incorrect solution for part 1')

    def test_example_solution_part2(self):
        result = day3.solve_part2()
        self.assertEqual(result, 3121910778619,
                         'Incorrect solution for part 2')


if __name__ == "__main__":
    unittest.main()
