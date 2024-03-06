import pytest


def test_raises_with():
    """ with を使って ValueError が発生するか確認 """
    with pytest.raises(ValueError):
        int('a')


def test_raises_not_with():
    """ ValueError が発生するか確認 """
    pytest.raises(ValueError, int, 'a')
