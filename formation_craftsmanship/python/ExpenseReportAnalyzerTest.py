import unittest

from ExpenseReportAnalyzer import ExpenseReportAnalyzer
from inputData import input_test, input_prod

#advent of code day 1 : https://adventofcode.com/2020/day/1
class ExpenseReportAnalyzerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.expense_report_analyzer_test = ExpenseReportAnalyzer(input_test)
        self.expense_report_analyzer_prod = ExpenseReportAnalyzer(input_prod)

    def test_part1(self):
        self.assertEqual(self.expense_report_analyzer_test.compute_anwswer(), 514579)
        self.assertEqual(self.expense_report_analyzer_prod.compute_anwswer(), 444019)

    def test_part2(self):
        self.assertEqual(self.expense_report_analyzer_test.compute_anwswer_part2(), 241861950)
        self.assertEqual(self.expense_report_analyzer_prod.compute_anwswer_part2(), 29212176)

    def test_returned_list_1721_and_299(self):
        self.assertContainsItems(self.expense_report_analyzer_test.get_target_couple(), 1721, 299)

    def test_that_three_entries_are_found(self):
        self.assertContainsItems(self.expense_report_analyzer_test.get_target_triplet(), 979, 366, 675)

    def test_that_prod_input_contains_nb1_nb2(self):
        self.assertContainsItems(self.expense_report_analyzer_prod.get_target_couple(), 251, 1769)

    def assertContainsItems(self, list_1, *expected_numbers):
        for number in expected_numbers:
            self.assertTrue(number in list_1)
        self.assertEqual(len(list_1), len(expected_numbers))

if __name__ == '__main__':
    unittest.main()
