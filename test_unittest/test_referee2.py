from unittest import TestCase
from janken.hands import rock, scissors, paper
from janken.player import User, CPU
from janken.referee import Referee


class TestReferee(TestCase):
    """Referee クラスのテスト"""

    def setUp(self):
        """テストメソッドの前処理"""
        self.user = User()
        self.cpu = CPU()
        self.referee = Referee()

    def test_user_win_rock_vs_scissors(self):
        """ユーザー勝利の判定テスト: グー vs チョキ"""
        self.user.hand = rock
        self.cpu.hand = scissors
        result = self.referee._is_user_win(self.user.hand, self.cpu.hand)
        self.assertTrue(result)

    def test_user_win_scissors_vs_paper(self):
        """ユーザー勝利の判定テスト: チョキ vs パー"""
        self.user.hand = scissors
        self.cpu.hand = paper
        result = self.referee._is_user_win(self.user.hand, self.cpu.hand)
        self.assertTrue(result)

    def test_user_win_paper_vs_rock(self):
        """ユーザー勝利の判定テスト: パー vs グー"""
        self.user.hand = paper
        self.cpu.hand = rock
        result = self.referee._is_user_win(self.user.hand, self.cpu.hand)
        self.assertTrue(result)

    def test_draw_rock_vs_rock(self):
        """引き分けの判定テスト: グー vs グー"""
        self.user.hand = rock
        self.cpu.hand = rock
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertFalse(self.referee.game_decided)

    def test_game_decided_user_win(self):
        """ゲーム決着の判定テスト: ユーザー勝利"""
        self.user.hand = scissors
        self.cpu.hand = paper
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertTrue(self.referee.game_decided)

    def test_game_decided_user_lose(self):
        """ゲーム決着の判定テスト: ユーザー敗北"""
        self.user.hand = paper
        self.cpu.hand = scissors
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertTrue(self.referee.game_decided)
