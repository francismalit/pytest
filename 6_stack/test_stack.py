import unittest
import sys
import os

from stack import Stack

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_size_0_after_create(self):
        self.assertEqual(self.stack.get_size(), 0)

    def test_push_increases_stack_size(self):
        ''' implement push method that takes one elemet as argument
        and increases stack size'''
        self.stack.push(1)
        self.assertEqual(self.stack.get_size(), 1)
        self.assertNotEqual(self.stack.get_size(), 0)

    ''' Do you have any duplication in your tests? How to remove it? '''

    def test_pop_decreases_stack_size(self):
        ''' implement pop that decreases stack size '''
        #self.assertEqual(self.stack.get_size(), 1)
        # self.stack.pop()
        # self.assertEqual(self.stack.get_size(), 1)
        self.assertEqual(self.stack.get_size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.get_size(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.get_size(), 0)

    def test_popping_empty_stack_returns_None(self):
        self.assertEqual(self.stack.get_size(), 0)
        self.assertEqual(self.stack.pop(), None)

    def test_when_1_pushed_pop_returns_1(self):
        ''' test pushing and popping 1 to stack '''
        self.assertEqual(self.stack.get_size(), 0)
        # self.test_pop_decreases_stack_size()
        self.assertEqual(self.stack.pop(1), None)

        pass
    
    def test_stack_works_as_lifo(self):
        ''' test pushing several items, they should pop in last in first out order '''
        pass
    
    ''' Do you think you can refactor your stack? '''


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
