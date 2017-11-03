import unittest
import number


class TestArithmetics(unittest.TestCase):

    def test_add_two_number(self):
        self.assertEqual(number.add(1, 2), 3)
        self.assertEqual(number.add(22, 13), 35)

    def test_multiply(self):
        # implement number.multiply
        self.assertEqual(number.multiply(1, 2), 2)
        self.assertEqual(number.multiply(22, 13), 286)
        pass

    def test_safe_division(self):
        # implement number.divide, that will return 0
        # when you divide with 0.
        zero = 0
        self.assertEqual(number.divide(1, zero), zero)
        self.assertEqual(number.divide(22, zero), zero)
        pass

    def test_add_many(self):
        self.assertEqual(number.add(1, 2, 1), 4)
        self.assertEqual(number.add(1, 1, 1, 1, 1, 1), 6)
        self.assertEqual(number.add(1), 1)
        # Modify number.add to add together
        # any number of arguments
        pass

    def test_multiply_should_handle_strings(self):
        self.assertEqual(number.multiply(1, 2), 2)
        self.assertEqual(number.multiply(1, 2, 3), 6)
        self.assertEqual(number.multiply(1, 2, 3, 0), 0)
        pass

    def test_add_two_largest(self):
        self.assertEqual(number.add_two_largest(1, 23, 33, 5, 100), 133)
        # Implement number.add_two_largest, that adds up 
        # together two largest numbers in its arguments
        pass


if __name__ == "__main__":
    unittest.main()
