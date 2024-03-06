from unittest import TestCase

from janken.hands import rock, scissors
from janken.player import User, CPU
from janken.referee import Referee
from janken.score import Score


class TestScore(TestCase):
    """ Score クラスのテスト """

    def setUp(self):
        """ 個々のテストでインスタンスを生成する """
        self.score = Score()

    def test_score_increment_win(self):
        """ 勝利数が正しく加算されるかテスト """
        self.score.increment_win()
        self.assertEqual(self.score.win, 1)
        self.assertEqual(self.score.lose, 0)

    def test_score_increment_lose(self):
        """ 敗北数が正しく加算されるかテスト """
        self.score.increment_lose()
        self.assertEqual(self.score.win, 0)
        self.assertEqual(self.score.lose, 1)

    def test_score_show(self):
        """ 成績が正しく表示されるかテスト """
        self.score.win = 3
        self.score.lose = 2
        self.assertEqual(self.score.show(), 'あなたの成績は 3勝 2敗 でした')


class TestUserScore(TestCase):
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

    def test_user_draw(self):
        """ ユーザーが引き分けたときのスコア計算 """
        self.user.hand = rock
        self.cpu.hand = rock
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertEqual(self.user.score.win, 0)
        self.assertEqual(self.user.score.lose, 0)
