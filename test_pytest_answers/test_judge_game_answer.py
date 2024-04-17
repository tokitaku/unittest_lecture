import pytest

from blackjack.main import GameManager
from blackjack.player import UserGameState


@pytest.mark.parametrize('user_score, dealer_score, expected_result', [
    (19, 16, UserGameState.WIN),  # ユーザーが勝つ
    (16, 19, UserGameState.LOSE),  # ディーラーが勝つ
    (16, 16, UserGameState.DRAW),  # 引き分け
    (22, 22, UserGameState.LOSE),  # 双方バーストでユーザーが負ける
])
def test_evaluate_game(self, user_score, dealer_score, expected_result):
    """勝敗判定のテスト"""
    self.manager = GameManager()
    self.user = self.manager.user
    self.dealer = self.manager.dealer

    self.user.score = user_score
    self.user.is_burst = user_score > 21

    self.dealer.score = dealer_score
    self.dealer.is_burst = dealer_score > 21

    self.manager.judge_helper._judge_game()

    assert self.user.game_result == expected_result
