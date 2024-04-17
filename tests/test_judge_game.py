import pytest

from blackjack.main import GameManager
from blackjack.player import UserGameState


class TestJudgeGame:
    """勝敗判定のテスト"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.manager = GameManager()
        self.user = self.manager.user
        self.dealer = self.manager.dealer

    def test_evaluate_game_user_win(self):
        """ユーザーが勝った場合の勝敗判定"""
        self.user.score = 19
        self.user.is_burst = False

        self.dealer.score = 16
        self.dealer.is_burst = False

        self.manager.judge_helper._judge_game()

        assert self.user.game_result == UserGameState.WIN

    def test_evaluate_game_user_lose(self):
        """ユーザーが負けた場合の勝敗判定"""
        self.user.score = 16
        self.user.is_burst = False

        self.dealer.score = 19
        self.dealer.is_burst = False

        self.manager.judge_helper._judge_game()

        assert self.user.game_result == UserGameState.LOSE

    def test_evaluate_game_user_draw(self):
        """引き分けた場合の勝敗判定"""
        self.user.score = 16
        self.user.is_burst = False

        self.dealer.score = 16
        self.dealer.is_burst = False

        self.manager.judge_helper._judge_game()

        assert self.user.game_result == UserGameState.DRAW

    def test_evaluate_game_user_and_dealer_burst(self):
        """双方がバーストした場合の勝敗判定"""
        self.user.score = 22
        self.user.is_burst = True

        self.dealer.score = 22
        self.dealer.is_burst = True

        self.manager.judge_helper._judge_game()

        assert self.user.game_result == UserGameState.LOSE
