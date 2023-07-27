import unittest
import main

class TestBinarySearch(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        self.assertEqual(main.binary_search(arr, 1), -1)

    def test_single_element_array(self):
        arr = [1]
        self.assertEqual(main.binary_search(arr, 1), 0)
        self.assertEqual(main.binary_search(arr, 2), -1)

    def test_even_length_array(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(main.binary_search(arr, 1), 0)
        self.assertEqual(main.binary_search(arr, 2), 1)
        self.assertEqual(main.binary_search(arr, 3), 2)
        self.assertEqual(main.binary_search(arr, 4), 3)
        self.assertEqual(main.binary_search(arr, 5), -1)

    def test_odd_length_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(main.binary_search(arr, 1), 0)
        self.assertEqual(main.binary_search(arr, 2), 1)
        self.assertEqual(main.binary_search(arr, 3), 2)
        self.assertEqual(main.binary_search(arr, 4), 3)
        self.assertEqual(main.binary_search(arr, 5), 4)
        self.assertEqual(main.binary_search(arr, 6), -1)

    def test_duplicate_elements(self):
        arr = [1, 2, 2, 3, 4, 4, 4, 5]
        self.assertEqual(main.binary_search(arr, 1), 0)
        self.assertEqual(main.binary_search(arr, 2), 1)
        self.assertEqual(main.binary_search(arr, 3), 3)
        self.assertEqual(main.binary_search(arr, 4), 4)
        self.assertEqual(main.binary_search(arr, 5), 7)
        self.assertEqual(main.binary_search(arr, 6), -1)

if __name__ == '__main__':
    unittest.main()