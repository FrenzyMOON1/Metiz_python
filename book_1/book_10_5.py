from book_10_5_0 import get_formatted_name
import unittest


class TestBook1050(unittest.TestCase):
    def test_first_last_name(self):
        self.assertEqual(get_formatted_name("John", "Doe"), "John Doe")
        self.assertEqual(get_formatted_name("Jane", "Doe", "faggot"), "Jane Faggot Doe")
        