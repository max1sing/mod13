import unittest
from datetime import datetime

def validate_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

def validate_chart_type(chart_type):
    return chart_type in ['1', '2']

def validate_time_series(time_series):
    return time_series in ['1', '2', '3', '4']

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class TestStockVisualizerInputs(unittest.TestCase):

    def test_symbol(self):
        self.assertTrue(validate_symbol("AAPL"))
        self.assertFalse(validate_symbol("aapl"))
        self.assertFalse(validate_symbol("AAPL123"))
        self.assertFalse(validate_symbol("A"))
    
    def test_chart_type(self):
        self.assertTrue(validate_chart_type("1"))
        self.assertTrue(validate_chart_type("2"))
        self.assertFalse(validate_chart_type("3"))
        self.assertFalse(validate_chart_type("a"))
    
    def test_time_series(self):
        self.assertTrue(validate_time_series("1"))
        self.assertTrue(validate_time_series("4"))
        self.assertFalse(validate_time_series("5"))
        self.assertFalse(validate_time_series("a"))
    
    def test_start_date(self):
        self.assertTrue(validate_date("2023-01-01"))
        self.assertFalse(validate_date("20230101"))
        self.assertFalse(validate_date("01-01-2023"))
        self.assertFalse(validate_date("2023/01/01"))
    
    def test_end_date(self):
        self.assertTrue(validate_date("2023-12-31"))
        self.assertFalse(validate_date("12-31-2023"))
        self.assertFalse(validate_date("2023-13-01"))
        self.assertFalse(validate_date("2023-02-30"))

if __name__ == '__main__':
    unittest.main()