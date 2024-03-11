import pytest

from blackjack.card import Card
from blackjack.player import Player


@pytest.fixture()
def setup():
    spade_king = Card('♠', 'K')  # 1. Card インスタンスの生成
    diamond_queen = Card('♦', 'Q')
    yield spade_king, diamond_queen


def test_calculate_score_20(setup):
    spade_king, diamond_queen = setup
    user = Player("test")
    user.hand = [spade_king, diamond_queen]  # 2. 手札にカードを追加
    user.calculate_score()  # 3. スコアを計算
    assert user.score == 20
