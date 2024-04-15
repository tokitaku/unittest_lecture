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
