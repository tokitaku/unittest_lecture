from unittest import TestCase

from janken.hands import rock, paper, scissors
from janken.player import CHOICES, Player


class TestPlayer(TestCase):
    """ Player 手のテスト (共通化しないパターン) """

    def test_choice_rock(self):
        """Player の手をグーに設定するテスト"""
        player = Player()
        player.hand = CHOICES['g']
        self.assertEqual(player.hand, rock)

    def test_choice_paper(self):
        """Player の手をパーに設定するテスト"""
        player = Player()
        player.hand = CHOICES['p']
        self.assertEqual(player.hand, paper)

    def test_choice_scissors(self):
        """Player の手をチョキに設定するテスト"""
        player = Player()
        player.hand = CHOICES['c']
        self.assertEqual(player.hand, scissors)
