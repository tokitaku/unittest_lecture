import pytest

from blackjack.card import Card
from blackjack.player import Player


def test_calculate_score_20():
    """手札のスコアが20点のテスト"""
    spade_king = Card('♠', 'K')  # 1. Card インスタンスの生成
    diamond_queen = Card('♦', 'Q')
    player = Player("test")
    player.hand = [spade_king, diamond_queen]  # 2. 手札にカードを追加
    player.calculate_score()  # 3. スコアを計算
    assert player.score == 20


class TestScoreByFixture:
    """手札のスコア計算のテスト(フィクスチャを使ったテスト)"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.player = Player("test")
        self.spade_king = Card("♠", "K")
        self.diamond_queen = Card("♦", "Q")
        self.hearts_ace = Card("♥", "A")
        self.club_9 = Card("♣", "9")

    def test_calculate_score_20(self):
        """手札のスコアが20点のテスト"""
        self.player.hand = [self.spade_king, self.diamond_queen]
        self.player.calculate_score()
        assert self.player.score == 20

    def test_calculate_score_19(self):
        """手札のスコアが19点のテスト"""
        self.player.hand = [self.spade_king, self.club_9]
        self.player.calculate_score()
        assert self.player.score == 19

    def test_calculate_score_21(self):
        """手札がナチュラルブラックジャック(21点)のテスト"""
        self.player.hand = [self.hearts_ace, self.spade_king]
        self.player.calculate_score()
        assert self.player.score == 21

    def test_calculate_natual_blackjack(self):
        """手札がナチュラルブラックジャック(21点)の状態テスト"""
        self.player.hand = [self.hearts_ace, self.spade_king]
        self.player.calculate_score()
        assert self.player.is_natural_blackjack is True


class TestScoreByMarkParametrize:
    """手札のスコア計算のテスト(マーク付きパラメータ化を使ったテスト)"""

    @pytest.mark.parametrize("hand, expected", [
        ([Card('♠', 'A'), Card('♦', 'A')], 12),
        ([Card('♠', '2'), Card('♦', '6')], 8),
        ([Card('♠', '3'), Card('♣', '7')], 10),
        ([Card('♥', '4'), Card('♠', '8')], 12),
        ([Card('♠', '5'), Card('♦', '9')], 14),
        ([Card('♠', '10'), Card('♦', 'J')], 20),
        ([Card('♠', 'Q'), Card('♣', 'K')], 20),
        ([Card('♥', 'A'), Card('♠', 'K')], 21),
        ([Card('♥', 'A'), Card('♠', 'K')], 21),
        ([Card('♠', 'A'), Card('♦', 'A'), Card('♣', 'A')], 13),
        ([Card('♠', 'A'), Card('♦', 'A'), Card('♣', 'A'), Card('♥', 'A')], 14),
        ([Card('♠', 'A'), Card('♦', '2'), Card('♣', '3'), Card('♥', '4'), Card('♠', 'K')], 20),
    ])
    def test_calculate_score(self, hand, expected):
        """手札のスコア計算のテスト"""
        player = Player("test")
        player.hand = hand
        player.calculate_score()
        assert player.score == expected

    @pytest.mark.parametrize("hand, expected", [
        ([Card('♥', 'K'), Card('♥', 'Q'), Card('♥', '2')], True),  # 22点
        ([Card('♥', 'A'), Card('♥', 'K')], False),  # 21点
        ([Card('♥', 'A'), Card('♠', '9')], False),  # 20点
        ([Card('♥', 'A'), Card('♠', 'A'), Card('♦', 'A')], False),  # 13点
    ])
    def test_is_burst(self, hand, expected):
        """プレイヤーがバーストしたかテスト"""
        player = Player("test")
        player.hand = hand
        player.calculate_score()
        assert player.is_burst == expected
