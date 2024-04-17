import pytest

from blackjack.main import GameManager
from blackjack.player import UserGameState


@pytest.mark.parametrize('user_score, dealer_score, expected', [
    (19, 16, UserGameState.WIN),  # ユーザーが勝つ
    (16, 19, UserGameState.LOSE),  # ディーラーが勝つ
    (16, 16, UserGameState.DRAW),  # 引き分け
    (22, 22, UserGameState.LOSE),  # 双方バーストでユーザーが負ける
])
def test_evaluate_game(user_score, dealer_score, expected):
    """勝敗判定のテスト"""
    manager = GameManager()
    user = manager.user
    dealer = manager.dealer

    user.score = user_score
    user.is_burst = user_score > 21

    dealer.score = dealer_score
    dealer.is_burst = dealer_score > 21

    manager.judge_helper._judge_game()

    assert user.game_result == expected
