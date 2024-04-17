import pytest

from blackjack.main import GameManager


class TestDealerHit:
    """ディーラーがヒットするかどうかのテスト"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.manager = GameManager()
        self.user = self.manager.user
        self.dealer = self.manager.dealer

    def test_dealer_should_hit_user_burst_and_17(self):
        """ディーラーがユーザーに得点で勝っていても17点未満の場合は引く"""
        self.user.score = 15
        self.user.is_burst = False
        self.dealer.score = 16
        self.dealer.is_burst = False

        assert self.manager.judge_helper.dealer_should_hit_card() is True

    def test_dealer_should_hit_user_burst(self):
        """ユーザーがバースト (21点を超える) し、ディーラーが17点未満の場合は引く"""
        self.user.score = 22
        self.user.is_burst = True
        self.dealer.score = 16
        self.dealer.is_burst = False

        assert self.manager.judge_helper.dealer_should_hit_card() is True

    def test_dealer_should_hit_dealer_lose(self):
        """ディーラーがユーザーに得点で負けている場合は引く"""
        self.user.score = 20
        self.user.is_burst = False
        self.dealer.score = 15
        self.dealer.is_burst = False

        assert self.manager.judge_helper.dealer_should_hit_card() is True

    def test_dealer_should_hit_tie(self):
        """ディーラーとユーザーが21点未満かつ同点の場合は引く"""
        self.user.score = 20
        self.user.is_burst = False
        self.dealer.score = 20
        self.dealer.is_burst = False

        assert self.manager.judge_helper.dealer_should_hit_card() is True

    def test_dealer_should_not_hit_dealer_burst(self):
        """ディーラーがバーストしている場合は引かない"""
        self.user.score = 20
        self.user.is_burst = False
        self.dealer.score = 22
        self.dealer.is_burst = True

        assert self.manager.judge_helper.dealer_should_hit_card() is False

    def test_dealer_should_not_hit_dealer_win(self):
        """ディーラーが17点以上かつユーザーに勝っている場合は引かない"""
        self.user.score = 15
        self.user.is_burst = False
        self.dealer.score = 20
        self.dealer.is_burst = False

        assert self.manager.judge_helper.dealer_should_hit_card() is False

    def test_dealer_should_not_hit_user_burst_and_17(self):
        """ユーザーがバーストし、ディーラーが17点以上の場合は引かない"""
        self.user.score = 22
        self.user.is_burst = True
        self.dealer.score = 17
        self.dealer.is_burst = False

        assert self.manager.judge_helper.dealer_should_hit_card() is False

    def test_dealer_should_not_hit_tie(self):
        """ユーザーが21点、ディーラーも21点の場合は引かない"""
        self.user.score = 21
        self.user.is_burst = False
        self.dealer.score = 21
        self.dealer.is_burst = False

        assert self.manager.judge_helper.dealer_should_hit_card() is False


class TestDealerHitByParametrize:
    """ディーラーがヒットするかどうかのテスト (parametrize を使用)"""

    @pytest.mark.parametrize("user_score, dealer_score, expected", [
        (15, 16, True),  # ディーラーがユーザーに得点で勝っていても17点未満の場合は引く
        (22, 16, True),  # ユーザーがバースト (21点を超える) し、ディーラーが17点未満の場合は引く
        (20, 15, True),  # ディーラーがユーザーに得点で負けている場合は引く
        (20, 20, True),  # ディーラーとユーザーが21点未満かつ同点の場合は引く
        (20, 22, False),  # ディーラーがバーストしている場合は引かない
        (15, 20, False),  # ディーラーが17点以上かつユーザーに勝っている場合は引かない
        (22, 17, False),  # ユーザーがバーストし、ディーラーが17点以上の場合は引かない
        (21, 21, False),  # ユーザーが21点、ディーラーも21点の場合は引かない
    ]
                             )
    def test_dealer_should_hit(self, user_score, dealer_score, expected):
        self.manager = GameManager()
        self.user = self.manager.user
        self.dealer = self.manager.dealer

        self.user.score = user_score
        self.user.is_burst = user_score > 21
        self.dealer.score = dealer_score
        self.dealer.is_burst = dealer_score > 21

        assert self.manager.judge_helper.dealer_should_hit_card() == expected
