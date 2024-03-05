from unittest import TestCase

from janken.hands import rock, scissors
from janken.player import User, CPU
from janken.referee import Referee


class TestScore(TestCase):
    """ 勝敗によってユーザーのスコアが正しく加算されるかテスト """

    def setUp(self):
        """ 個々のテストでインスタンスを生成する """
        self.user = User()
        self.cpu = CPU()
        self.referee = Referee()

    def test_user_win(self):
        """ ユーザーが勝利したときのスコア計算 """
        self.user.hand = rock
        self.cpu.hand = scissors
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertEqual(self.user.score.win, 1)
        self.assertEqual(self.user.score.lose, 0)

    def test_user_lose(self):
        """ ユーザーが敗北したときのスコア計算 """
        self.user.hand = scissors
        self.cpu.hand = rock
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertEqual(self.user.score.win, 0)
        self.assertEqual(self.user.score.lose, 1)
