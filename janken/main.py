from janken.player import User, CPU
from janken.referee import Referee


def graceful_exit(user: User):
    """Ctrl+Cで終了されたときにプログラムを終了させる関数"""
    print("ゲームを終了します。")
    print(user.score.show())
    exit()


def is_user_replay_decision():
    """ユーザーに再戦するかどうか尋ねる関数"""
    return bool(input('再戦する場合は何か入力してエンターキーを押してください: '))


def print_results(user, cpu, referee):
    """結果を表示する関数"""
    print(f'あなた: {user.hand.art}')
    print(f'コンピュータ: {cpu.hand.art}')
    print(f"{referee.judgment_result}\n")


def round_of_game(user, cpu, referee):
    """じゃんけんを一回実行する関数"""
    user.choice_hand()
    cpu.choice_hand()
    referee.evaluate_judge(user, cpu)
    print_results(user, cpu, referee)


def play_rounds(user, cpu, referee):
    """じゃんけんの各ラウンドをプレイする関数"""
    while True:
        print("\nじゃんけん！")
        # 決着がつくまで繰り返す
        while not referee.game_decided:
            round_of_game(user, cpu, referee)
        if not is_user_replay_decision():
            break
        referee.reset_game()


def play_game():
    """じゃんけんを実行する関数"""
    user = User()
    cpu = CPU()
    referee = Referee()

    try:
        play_rounds(user, cpu, referee)
    except KeyboardInterrupt:
        graceful_exit(user)

    print(user.score.show())
    print('またね！')


# じゃんけんを実行
if __name__ == '__main__':
    play_game()
