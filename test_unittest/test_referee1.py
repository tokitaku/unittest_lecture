from unittest import TestCase

from janken.hands import rock, paper
from janken.player import User, CPU
from janken.referee import Referee


class TestReferee(TestCase):
    """ Referee のテスト """

    def test_judge_message_win(self):
        """ 勝利メッセージのテスト """

        self.user = User()
        self.user.hand = paper

        self.cpu = CPU()
        self.cpu.hand = rock

        self.referee = Referee()
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertEqual(self.referee.judgment_result, "勝ち！")

    def test_judge_message_lose(self):
        """ 敗北メッセージのテスト """
        self.user = User()
        self.user.hand = rock

        self.cpu = CPU()
        self.cpu.hand = paper

        self.referee = Referee()
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertEqual(self.referee.judgment_result, "負け")

    def test_judge_message_draw(self):
        """ 引き分けメッセージのテスト """
        self.user = User()
        self.user.hand = rock

        self.cpu = CPU()
        self.cpu.hand = rock

        self.referee = Referee()
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertEqual(self.referee.judgment_result, "あいこ")
