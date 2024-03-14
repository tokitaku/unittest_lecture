from unittest import TestCase


class TestUnitTestClass(TestCase):
    """ unittest のテストクラス """

    def test_raise_with(self):
        """ ValueError が発生するか確認 """
        with self.assertRaises(ValueError):
            int('a')

    def test_raise_not_with(self):
        """ ValueError が発生するか確認 """
        self.assertRaises(ValueError, int, 'a')


