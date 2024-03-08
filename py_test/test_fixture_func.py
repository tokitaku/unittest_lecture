import pytest

from janken.hands import rock


@pytest.fixture
def setup():
    rock_art = rock
    yield rock_art


def test_rock(setup):
    print(setup.art)
    assert setup == rock


def test_rock_name(setup):
    print(f"\n{setup.name}")
    assert setup.name == "グー"
