import unittest
from utils import (
    example_utils_function,
    format_account_number,
    get_current_datetime
)
from masks import mask_card_number, mask_account_number


class TestUtilsFunctions(unittest.TestCase):
    def test_example_utils_function(self):
        self.assertEqual(example_utils_function(5), 10)

    def test_format_account_number(self):
        self.assertEqual(
            format_account_number("12345678901234567890"),
            "Счет **7890")
        with self.assertRaises(ValueError):
            format_account_number("invalid")

    def test_get_current_datetime(self):
        datetime_str = get_current_datetime()
        self.assertEqual(len(datetime_str), 19)


class TestMasksFunctions(unittest.TestCase):
    def test_mask_card_number(self):
        self.assertEqual(
            mask_card_number("1234567890123456"),
            "1234 56** **** 3456")
        with self.assertRaises(ValueError):
            mask_card_number("1234")

    def test_mask_account_number(self):
        self.assertEqual(
            mask_account_number("12345678901234567890"),
            "**7890")
        with self.assertRaises(ValueError):
            mask_account_number("1234")


if __name__ == "__main__":
    unittest.main()
