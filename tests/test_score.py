import pytest

from blackjack.card import Card
from blackjack.player import Player


@pytest.fixture()
def setup():
    hertz_ace = Card('♥', 'A')  # 1. Card インスタンスの生成
    spade_king = Card('♠', 'K')
    club_9 = Card('♣', '9')
    yield hertz_ace, spade_king, club_9


def test_calculate_score_20(setup):
    """スコアが正しく計算されているかテスト (20点)"""
    hertz_ace, spade_king, club_9 = setup
    user = Player("test")
    user.hand = [hertz_ace, spade_king, club_9]  # 2. 手札にカードを追加
    user.calculate_score()  # 3. スコアを計算
    assert user.score == 20
