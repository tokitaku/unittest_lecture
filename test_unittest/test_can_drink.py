from unittest import TestCase


def can_drink_alcohol(age):
    """
    引数 age を受け取り、20以上なら '飲酒可能です' という文字列を返す

    age が float の場合は TypeError を発生させる
    age が整数でない場合は TypeError を発生させる
    age が負の数の場合は ValueError を発生させる
    age が20未満の場合は ValueError を発生させる

    :param age: int
    :return: str
    """

    if isinstance(age, float):
        raise TypeError("整数を入力してください")
    elif not isinstance(age, int):
        raise TypeError("整数以外は判定できません")
    elif age < 0:
        raise ValueError("正の数を入力してください")
    elif age < 20:
        raise ValueError("飲酒不可です")

    return "飲酒可能です"


class TestCanDrinkAlcohol(TestCase):
    """ can_drink_alcohol() のテスト """

    def test_can_drink(self):
        """ 飲酒可能な年齢の場合のテスト"""
        self.assertEqual(can_drink_alcohol(20), "飲酒可能です")
        self.assertEqual(can_drink_alcohol(30), "飲酒可能です")

    def test_float(self):
        """ float の場合のテスト"""
        with self.assertRaises(TypeError) as e:
            can_drink_alcohol(20.5)
        self.assertEqual(str(e.exception), "整数を入力してください")

    def test_non_integer(self):
        """ 整数以外の場合のテスト"""
        with self.assertRaises(TypeError) as e:
            can_drink_alcohol("20")
        self.assertEqual(str(e.exception), "整数以外は判定できません")

        with self.assertRaises(TypeError) as e:
            can_drink_alcohol([20])
        self.assertEqual(str(e.exception), "整数以外は判定できません")

    def test_negative_age(self):
        """ 負の数の場合のテスト"""
        with self.assertRaises(ValueError) as e:
            can_drink_alcohol(-1)
        self.assertEqual(str(e.exception), "正の数を入力してください")

    def test_under_age(self):
        """ 20未満の場合のテスト"""
        with self.assertRaises(ValueError) as e:
            can_drink_alcohol(19)
        self.assertEqual(str(e.exception), "飲酒不可です")
