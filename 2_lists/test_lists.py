import unittest
import lst


class TestLists(unittest.TestCase):

    def test_sort_list(self):
        self.assertEquals(lst.sort(2, 1, 3, 7), [1, 2, 3, 7])
        self.assertEquals(lst.sort(2, -7), [-7, 2])

    def test_find_largest_value(self):
        self.assertEquals(lst.maximum(2, 1, 3, 7), [7])
        # implement lst.maximum (note that is should handle also
        # numbers that are given as strings)

    def test_only_positives(self):
        self.assertEquals(lst.positives(2, 1, 3, 7), [2, 1, 3, 7])
        self.assertEquals(lst.positives(-5, 0, 2, 1, 3, 7, -1,), [0, 2, 1, 3, 7])
        # implement lst.positives, which will return a list without
        # negative numbers


if __name__ == "__main__":
    unittest.main()
