import pytest

from blackjack.deal_helper import Odds
from blackjack.main import GameManager


class TestOdds:
    """掛け金分配率のテスト"""

    @pytest.mark.parametrize('user_score, dealer_score, expected_result', [
        (21, 20, Odds.NATURAL_BLACK_JACK.value),  # ユーザーのナチュラルブラックジャック
        (19, 16, Odds.WIN.value),  # ユーザーの勝ち
        (16, 19, Odds.LOSE.value),  # ユーザーの負け
        (16, 16, Odds.DRAW.value),  # 引き分け
    ])
    def test_evaluate_game(self, user_score, dealer_score, expected_result):
        """勝敗判定のパラメータ化テスト"""
        self.manager = GameManager()
        self.user = self.manager.user
        self.dealer = self.manager.dealer

        self.user.score = user_score
        self.user.is_natural_blackjack = user_score == 21

        self.dealer.score = dealer_score
        self.manager.judge_helper.evaluate_judge()

        assert self.user.bet_distribute_rate == expected_result
