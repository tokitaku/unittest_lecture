import pytest

from blackjack.card import Card


def test_card_score_ace():
    """Aのスコアが11点のテスト"""
    card = Card('♠', 'A')
    assert card.score == 11


class TestCardScore:
    """カードのスコアのテスト"""

    @pytest.mark.parametrize('rank, expected', [
        ('A', 11),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
        ('7', 7),
        ('8', 8),
        ('9', 9),
        ('10', 10),
        ('J', 10),
        ('Q', 10),
        ('K', 10),
    ])
    def test_card_score(self, rank, expected):
        """カードのスコアのテスト"""
        card = Card('♠', rank)
        assert card.score == expected
