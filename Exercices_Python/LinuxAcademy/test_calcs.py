import unittest

import calcs


class TestCalcs(unittest.TestCase):
    def test_circle_circumference(self):
        # values includes radii and the expected circumference
        values = [
            (10.2, 64.09),
            (5.67, 35.63),
            (100, 628.32),
            (75.25, 472.81),
            (95, 596.91),
        ]

        for radius, circumference in values:
            self.assertEqual(calcs.circle_circumference(radius), circumference)

    def test_circle_area(self):
        # values includes radii and the expected area
        values = [
            (10.2, 326.86),
            (5.67, 101.00),
            (100, 31415.93),
            (75.25, 17789.47),
            (94, 27759.12),
        ]

        for radius, area in values:
            self.assertEqual(calcs.circle_area(radius), area)


if __name__ == "__main__":
    unittest.main()
