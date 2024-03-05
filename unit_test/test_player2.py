from unittest import TestCase

from janken.hands import rock, paper, scissors
from janken.player import CHOICES, Player


class TestPlayerCommonality(TestCase):
    """ Player 手のテスト (共通化するパターン) """

    @classmethod
    def setUpClass(cls):
        """ テストクラスの前処理 テスト実行時に最初に一度だけ実行される"""
        print("\nsetUpClass\n")

    @classmethod
    def tearDownClass(cls):
        """ テストクラスの後処理 テスト実行時に最後に一度だけ実行される"""
        print("\ntearDownClass")

    def setUp(self):
        """ テストメソッドの前処理 それぞれのテストメソッドの前に実行される"""
        print("\nsetUp")
        self.player = Player()

    def tearDown(self):
        """ テストメソッドの後処理 それぞれのテストメソッドの後に実行される """
        print("tearDown")

    def test_choice_rock(self):
        """Player の手をグーに設定するテスト"""
        self.player.hand = CHOICES['g']
        self.assertEqual(self.player.hand, rock)

    def test_choice_paper(self):
        """Player の手をパーに設定するテスト"""
        self.player.hand = CHOICES['p']
        self.assertEqual(self.player.hand, paper)

    def test_choice_scissors(self):
        """Player の手をチョキに設定するテスト"""
        self.player.hand = CHOICES['c']
        self.assertEqual(self.player.hand, scissors)
