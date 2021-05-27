import unittest


# 4L de jacky
# le compteur kilométrique de la 4L de jacky est tout neuf
# quand le compteur affiche 222222 on retourne True
# quand le compteur affiche 444444 on retourne True
# quand le compteur affiche 738922 on retourne False
# quand le compteur affiche 051968 on retourne True
from Odometer import Odometer, is_interesting


class OdometerTest(unittest.TestCase):
    def test_that_all_figures_are_the_same(self):
        self.assertEqual(is_interesting(Odometer(222222)), True)
        self.assertEqual(is_interesting(Odometer(111111)), True)
        self.assertEqual(is_interesting(Odometer(333333)), True)
        self.assertEqual(is_interesting(Odometer(555555)), True)

    def test_that_all_figures_are_not_interesting_if_do_not_fill_odometer_length(self):
        self.assertEqual(is_interesting(Odometer(5555)), False)


    def test_that_boring_numbers_arent_interesting(self):
        self.assertEqual(is_interesting(Odometer(738922)), False)
        self.assertEqual(is_interesting(Odometer(123458)), False)
        self.assertEqual(is_interesting(Odometer(628333)), False)
        self.assertEqual(is_interesting(Odometer(111112)), False)

    def test_that_may_1968_is_interesting(self):
        self.assertEqual(is_interesting(Odometer(51968)), True)

    def test_that_69_is_in_figures(self):
        self.assertEqual(is_interesting(Odometer(12698)), True)
        self.assertEqual(is_interesting(Odometer(69)), True)


if __name__ == '__main__':
    unittest.main()
