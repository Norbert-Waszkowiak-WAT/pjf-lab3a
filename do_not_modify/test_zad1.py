import io
import re
import unittest
from unittest.mock import patch

from zad1 import double_value, triple_value, make_power

import inspect

def check_for_operators(func):
    source_code = inspect.getsource(func)
    return '+' in source_code or '*' in source_code

class TestZad1(unittest.TestCase):

    def test_double_value(self):
        self.assertEqual(double_value(5), 10)
        self.assertEqual(double_value(0), 0)
        self.assertEqual(double_value(-2), -4)
        self.assertFalse(check_for_operators(double_value))

    def test_triple_value(self):
        self.assertEqual(triple_value(5), 15)
        self.assertEqual(triple_value(0), 0)
        self.assertEqual(triple_value(-2), -6)
        self.assertFalse(check_for_operators(triple_value))

    def test_make_power(self):
        power = make_power()
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 5), 0)

        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            power(2, 3)

        stdout = fake_stdout.getvalue()
        match = re.search(r'Function power took .+ seconds to run.', stdout)
        self.assertIsNotNone(match)

if __name__ == '__main__':
    unittest.main()
