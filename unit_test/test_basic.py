from unittest import TestCase


class TestUnitTestClass(TestCase):
    """ unit_test のテストクラス """

    def test_method(self):
        """ unit_test のテストメソッド """
        self.assertEqual(2, 2)

    def test_method_2(self):
        """ unit_test のテストメソッド """
        self.assertIsNone(None)

    def test_method_3(self):
        """ unit_test のテストメソッド """
        assert 1 == 1
