import pytest

from blackjack.card import Card
from blackjack.player import Player


def test_calculate_score_20():
    spade_king = Card('♠', 'K')  # 1. Card インスタンスの生成
    diamond_queen = Card('♦', 'Q')
    user = Player("test")
    user.hand = [spade_king, diamond_queen]  # 2. 手札にカードを追加
    user.calculate_score()  # 3. スコアを計算
    assert user.score == 20
