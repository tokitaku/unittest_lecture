from janken.hands import rock, paper, scissors
from janken.player import User, CPU


class Referee:
    """勝敗を判定するクラス"""

    # 勝敗の組み合わせ
    winning_combinations = {
        # 勝ち手: 負け手
        rock: scissors,
        scissors: paper,
        paper: rock
    }

    def __init__(self):
        self.game_decided = False
        self.judgment_result = ""

    @classmethod
    def _is_user_win(cls, user_hand, computer_hand):
        return cls.winning_combinations[user_hand] == computer_hand

    def evaluate_judge(self, user: User, cpu: CPU):
        """
        じゃんけんの勝敗を判定する
        :param user: ユーザーのインスタンス
        :param cpu: コンピュータのインスタンス
        """

        if user.hand == cpu.hand:
            self.game_decided = False
            self.judgment_result = "あいこ"
        elif self._is_user_win(user.hand, cpu.hand):
            user.score.increment_win()
            self.game_decided = True
            self.judgment_result = "勝ち！"
        else:
            user.score.increment_lose()
            self.game_decided = True
            self.judgment_result = "負け"

    def reset_game(self):
        """ゲームをリセットする"""
        self.game_decided = False
        self.judgment_result = ""
