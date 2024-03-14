import pytest

from test_unittest.test_can_drink import can_drink_alcohol


def test_can_drink():
    """ 飲酒可能な年齢の場合のテスト"""
    assert can_drink_alcohol(20) == "飲酒可能です"
    assert can_drink_alcohol(30) == "飲酒可能です"


def test_float():
    """ float の場合のテスト"""
    with pytest.raises(TypeError) as e:
        can_drink_alcohol(20.5)
    assert str(e.value) == "整数を入力してください"


class TestCanDrinkAlcohol:
    """ can_drink_alcohol() のテスト """

    def test_non_integer(self):
        """ 整数以外の場合のテスト"""
        with pytest.raises(TypeError) as e:
            can_drink_alcohol("20")
        assert str(e.value) == "整数以外は判定できません"

        with pytest.raises(TypeError) as e:
            can_drink_alcohol([20])
        assert str(e.value) == "整数以外は判定できません"

    def test_negative_age(self):
        """ 負の数の場合のテスト"""
        with pytest.raises(ValueError) as e:
            can_drink_alcohol(-1)
        assert str(e.value) == "正の数を入力してください"

    def test_under_age(self):
        """ 20未満の場合のテスト"""
        with pytest.raises(ValueError) as e:
            can_drink_alcohol(19)
        assert str(e.value) == "飲酒不可です"
