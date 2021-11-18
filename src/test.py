import unittest

from utils.calculator import calculate_hours, get_value_by_hour, hour_in_range, calculate_salary
from utils.file_utils import read_data_file
import datetime as dt

case = unittest.TestCase()

class TestCalculator(unittest.TestCase):
    def test_calculate_hours(self):
        self.assertEqual(calculate_hours((dt.time(20,0), dt.time(21,0))), 1)
        self.assertEqual(calculate_hours((dt.time(10,0), dt.time(12,0))), 2)

    def test_get_value_by_hour(self):
        self.assertEqual(get_value_by_hour(dt.time(10,0), 'MO'), 15)
        self.assertEqual(get_value_by_hour(dt.time(20,0), 'SU'), 25)

    def test_hour_in_range(self):
        self.assertTrue(hour_in_range(dt.time(10,0), dt.time(10,0), dt.time(12,0)))
        self.assertFalse(hour_in_range(dt.time(9,0), dt.time(10,0), dt.time(12,0)))
    
    def test_read_data_file(self):
        self.assertRaises(FileNotFoundError, read_data_file, 'test.txt')
    
    def test_calculate_salary(self):
        data = read_data_file('data.txt')
        keys = list(data.keys())
        self.assertEqual(calculate_salary(data[keys[0]]), 215)
        self.assertEqual(calculate_salary(data[keys[1]]), 85)


if __name__ == '__main__':
    unittest.main()