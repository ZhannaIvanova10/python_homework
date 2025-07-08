import unittest
from utils import example_utils_function
from masks import example_masks_function


class TestFunctions(unittest.TestCase):
    def test_example_utils_function(self):
        self.assertEqual(example_utils_function(5), 10)

    def test_example_masks_function(self):
        self.assertEqual(example_masks_function("test"), "test_masked")


if __name__ == "__main__":
    unittest.main()
