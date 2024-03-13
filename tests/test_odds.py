import pytest

from blackjack.deal_helper import Odds
from blackjack.main import GameManager


class TestOdds:
    """掛け金分配率のテスト"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.manager = GameManager()
        self.user = self.manager.user
        self.dealer = self.manager.dealer

    def test_odds_natural_bj(self):
        """ナチュラルブラックジャックの掛け金分配率テスト"""
        self.user.is_natural_blackjack = True
        self.user.score = 21
        self.dealer.score = 20
        self.manager.judge_helper.evaluate_judge()
        assert self.user.bet_distribute_rate == Odds.NATURAL_BLACK_JACK.value

    def test_odds_win(self):
        """ユーザー勝利時の掛け金分配率テスト"""
        self.user.is_natural_blackjack = False
        self.user.score = 20
        self.dealer.score = 19
        self.manager.judge_helper.evaluate_judge()
        assert self.user.bet_distribute_rate == Odds.WIN.value

    def test_odds_draw(self):
        """引き分け時の掛け金分配率テスト"""
        self.user.is_natural_blackjack = False
        self.user.score = 20
        self.dealer.score = 20
        self.manager.judge_helper.evaluate_judge()
        assert self.user.bet_distribute_rate == Odds.DRAW.value

    def test_odds_lose(self):
        """ユーザー敗北時の掛け金分配率テスト"""
        self.user.is_natural_blackjack = False
        self.user.score = 19
        self.dealer.score = 20
        self.manager.judge_helper.evaluate_judge()
        assert self.user.bet_distribute_rate == Odds.LOSE.value

