import pytest

from blackjack.main import GameManager


class TestDealerHit:
    """ディーラーがヒットするかどうかのテスト"""

    @pytest.fixture(autouse=True)
    def setup_game_manager(self):
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

    def test_dealer_should_not_hit_dealer_burst(self):
        """ディーラーがバーストしている場合は引かない"""
        self.user.score = 20
        self.user.is_burst = False
        self.dealer.score = 22
        self.dealer.is_burst = True

        assert self.manager.judge_helper.dealer_should_hit_card() is False

    def test_dealer_should_not_hit_dealer_win(self):
        """ディーラーが17点以上かつユーザーに勝っている場合は引かない"""
        self.user.score = 18
        self.user.is_burst = False
        self.dealer.score = 19
        self.dealer.is_burst = False

        assert self.manager.judge_helper.dealer_should_hit_card() is False

    def test_dealer_should_not_hit_user_burst_and_17(self):
        """ユーザーがバーストし、ディーラーが17点以上の場合は引かない"""
        self.user.score = 22
        self.user.is_burst = True
        self.dealer.score = 17
        self.dealer.is_burst = False

        assert self.manager.judge_helper.dealer_should_hit_card() is False

    def test_dealer_should_not_hit_user_win(self):
        """ユーザーが21点、ディーラーも21点の場合は引かない"""
        self.user.score = 21
        self.user.is_burst = False
        self.dealer.score = 21
        self.dealer.is_burst = False

        assert self.manager.judge_helper.dealer_should_hit_card() is False

    def test_dealer_should_hit_tie(self):
        """ディーラーとユーザーが21点未満かつ同点の場合は引く"""
        self.user.score = 20
        self.user.is_burst = False
        self.dealer.score = 20
        self.dealer.is_burst = False

        assert self.manager.judge_helper.dealer_should_hit_card() is True

    @pytest.mark.parametrize('user_score, dealer_score, is_burst, expected', [
        # ディーラーが引くパターン
        (15, 16, {"user": False, "dealer": False}, True),  # ディーラーがユーザーに得点で勝っていても17点未満の場合は引く
        (22, 16, {"user": True, "dealer": False}, True),  # ユーザーがバースト (21点を超える) し、ディーラーが17点未満の場合は引く
        # ディーラーが引かないパターン
        (18, 19, {"user": False, "dealer": False}, False),  # ディーラーが17点以上かつユーザーに勝っている場合は引かない
        (22, 17, {"user": True, "dealer": False}, False),  # ユーザーがバーストし、ディーラーが17点以上の場合は引かない
        (21, 21, {"user": False, "dealer": False}, False),  # ユーザーが21点、ディーラーも21点の場合は引かない
        (20, 20, {"user": False, "dealer": False}, True),  # ディーラーとユーザーが21点未満かつ同点の場合は引く
    ])
    def test_dealer_hit(self, user_score, dealer_score, is_burst, expected):
        """ディーラーがカードを引くべきかどうかのテスト"""
        manager = GameManager()
        manager.user.score = user_score
        manager.user.is_burst = is_burst["user"]
        manager.dealer.score = dealer_score
        manager.dealer.is_burst = is_burst["dealer"]

        assert manager.judge_helper.dealer_should_hit_card() is expected
