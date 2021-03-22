#TestCheckSeason
import unittest
import CheckSeason

class KnownValues(unittest.TestCase):
    def test_season_for_winter(self):
        result = CheckSeason.checkSeason("January")
        expected = "Winter"
        self.assertEqual(expected, result)
    def test_season_for_spring(self):
        result = CheckSeason.checkSeason("March")
        expected = "Spring"
        self.assertEqual(expected, result)
    def test_season_for_summer(self):
        result = CheckSeason.checkSeason("July")
        expected = "Summer"
        self.assertEqual(expected, result)
    def test_season_for_fall(self):
        result = CheckSeason.checkSeason("September")
        expected = "Fall"
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
