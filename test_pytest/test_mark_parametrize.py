import pytest

from janken.hands import rock, scissors, paper
from janken.player import User, CPU
from janken.referee import Referee


class TestReferee:
    # 同じ構造のテストを実行する場合、pytest.mark.parametrize を使うとコードの重複を減らせます
    # 第一引数には文字列でテストメソッドに渡す引数名を文字列指定し、第二引数にはリストで引数の値を指定します
    @pytest.mark.parametrize("user_hand, cpu_hand, expected", [
        (rock, scissors, True),  # ユーザーがグー、CPUがチョキでユーザーが勝つケース
        (scissors, paper, True),  # ユーザーがチョキ、CPUがパーでユーザーが勝つケース
        (paper, rock, True),  # ユーザーがパー、CPUがグーでユーザーが勝つケース
        (rock, paper, False),  # ユーザーがグー、CPUがパーでユーザーが負けるケース
        (scissors, rock, False),  # ユーザーがチョキ、CPUがグーでユーザーが負けるケース
        (paper, scissors, False),  # ユーザーがパー、CPUがチョキでユーザーが負けるケース
    ])
    def test_is_user_win_lose_result(self, user_hand, cpu_hand, expected):
        """ 勝敗判定のテスト"""
        referee = Referee()
        result = referee._is_user_win(user_hand, cpu_hand)
        assert result == expected
        print(f"\nユーザーの手: {user_hand.name} / CPUの手: {cpu_hand.name} / ユーザーの勝ち？: {result}")

    # 以下のように第一引数をイテラブルで指定することもできます
    @pytest.mark.parametrize(["user_hand", "cpu_hand", "expected"], [
        (paper, rock, "勝ち！"),
        (rock, paper, "負け"),
        (scissors, scissors, "あいこ"),
    ])
    def test_judge_message(self, user_hand, cpu_hand, expected):
        """ 勝敗メッセージのテスト """
        user = User()
        user.hand = user_hand

        cpu = CPU()
        cpu.hand = cpu_hand

        referee = Referee()
        referee.evaluate_judge(user, cpu)

        assert referee.judgment_result == expected
        print(f"\nユーザーの手: {user_hand.name} / CPUの手: {cpu_hand.name} / 勝敗: {expected}")
