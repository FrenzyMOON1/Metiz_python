import unittest
from work_1 import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("John", "Doe", 10000)

    def test_give_default_raise(self):
        self.assertEqual(self.employee.give_raise(), 15000)

    def test_give_custom_raise(self):
        self.assertEqual(self.employee.give_raise(2000), 12000)


if __name__ == '__main__':
    unittest.main()
