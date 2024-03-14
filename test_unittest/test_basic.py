from unittest import TestCase


def add(a, b):
    return a + b


def return_none():
    return None


class TestUnitTestClass(TestCase):
    """ test_unittest のテストクラス """

    def test_method(self):
        """ add のテスト """
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_method_2(self):
        """ return_none のテスト """
        result = return_none()
        self.assertIsNone(result)

    def test_method_3(self):
        """ add のテスト"""
        result = add(1, 2)
        assert result == 3
