import pytest

from blackjack.deal_helper import Odds
from blackjack.main import GameManager


@pytest.mark.parametrize('user_score, dealer_score, expected', [
    (21, 20, Odds.NATURAL_BLACK_JACK.value),  # ユーザーのナチュラルブラックジャック
    (19, 16, Odds.WIN.value),  # ユーザーの勝ち
    (16, 19, Odds.LOSE.value),  # ユーザーの負け
    (16, 16, Odds.DRAW.value),  # 引き分け
])
def test_evaluate_game(user_score, dealer_score, expected):
    """掛け金分配率のテスト"""
    manager = GameManager()
    user = manager.user
    dealer = manager.dealer

    user.score = user_score
    user.is_natural_blackjack = user_score == 21

    dealer.score = dealer_score
    manager.judge_helper.evaluate_judge()

    assert user.bet_distribute_rate == expected
