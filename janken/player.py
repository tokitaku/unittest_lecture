from abc import ABC, abstractmethod
import random

from .hands import rock, paper, scissors
from .score import Score

# プレイヤーの選択肢
CHOICES = {
    'g': rock,
    'c': scissors,
    'p': paper
}


class Player(ABC):
    """プレイヤーの基底クラス"""

    def __init__(self):
        self.hand = None  # Hand クラスのインスタンス

    def choice_hand(self):
        """プレイヤーの手を選択するための抽象メソッド"""
        pass


class User(Player):
    """ユーザーのクラス"""

    def __init__(self):
        super().__init__()
        self.score = Score()

    def choice_hand(self):
        """
        ユーザーの手を選択するためのメソッド。
        ユーザーに手を入力してもらい、妥当な手が選択されるまでループする。
        """

        print("あなたの手をアルファベットで入力してください。")
        choices = "".join(f'{key}: {hand.name}\n' for key, hand in CHOICES.items())
        choice = ''
        while choice not in CHOICES:
            choice = input(f'{choices}').lower()
            if choice not in CHOICES:
                print(f'{" ".join(CHOICES)} のいずれかを入力してください。\n')
        self.hand = CHOICES[choice]


class CPU(Player):
    """コンピュータのクラス"""

    def choice_hand(self):
        """ コンピュータの手をランダムに選択するためのメソッド。 """

        self.hand = random.choice(list(CHOICES.values()))
