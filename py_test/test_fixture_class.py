import pytest

from janken.hands import rock, scissors, paper


class TestHandName:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.rock_art = rock
        self.paper_art = paper
        self.scissors_art = scissors
        yield

    def test_rock_name(self):
        print(self.rock_art.art)
        assert self.rock_art.name == "グー"

    def test_scissors_name(self):
        print(self.scissors_art.art)
        assert self.scissors_art.name == "チョキ"

    def test_paper_name(self):
        print(self.paper_art.art)
        assert self.paper_art.name == "パー"


