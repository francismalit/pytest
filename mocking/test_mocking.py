import unittest
import mock
import mockTest

sut = mockTest.SUT


class TestMocking(unittest.TestCase):

    def test_sut(self):
        sut.len = mock.Mock()
        assert sut.method()
