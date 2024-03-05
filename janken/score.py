class Score:
    def __init__(self):
        self.win = 0
        self.lose = 0

    def increment_win(self):
        self.win += 1

    def increment_lose(self):
        self.lose += 1

    def show(self):
        return f'あなたの成績は {self.win}勝 {self.lose}敗 でした'
