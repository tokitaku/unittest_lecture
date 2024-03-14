def test_func():
    """ pytest のテスト関数 """
    assert 2 == 2


class TestPyTestClass:
    """ pytest のテストクラス """

    def test_method(self):
        """ pytest のテストメソッド """
        assert 2 == 2

    def test_method_2(self):
        """ pytest のテストメソッド """
        assert "foo" == "foo"
