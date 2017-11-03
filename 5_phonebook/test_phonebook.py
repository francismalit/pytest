import unittest
import phone_book


# Exercise: Write a Phonebook using TDD
#
# 1. Add / get / update phonebook:
#    phone_book.add("John Doe", "+4989515912345")
#    number = phone_book.get(name)
#
#    Questions to be considered for the design:
#    What if a name does not exist (get)?
#    What if a name already exists (add)?
#    Should you test add and get independently?
#
# 2. Make phone_book persistent:
#    phone_book.load(filename)
#    phone_book.save(filename)
#
# 3. Advanced features:
#    Allow only valid names and numbers.
#    Invalid: "John Doe3", "+49", "+63xx1252342"


class TestPhonebook(unittest.TestCase):
    pass

    def test_save_phone_book(self):
        # self.assertEqual(phone_book.add("John Doe", "+4989515912345"), True)
        self.assertEqual(phone_book.save("test_phone_book.txt"), True)
        # self.assertEqual(phone_book.add(22, 13), 35)


    # def test_load_phone_book(self):
    # def test_add_phone_book(self):
    # def test_get_phone_book(self):

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
