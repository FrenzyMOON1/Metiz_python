import unittest
from book_10_5_1 import get_city


class TestGetCity(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(get_city("new", "york"), 'New York')

    def test_city_country_population(self):
        self.assertEqual(get_city("new", "york", "500"), "New York - 500")
