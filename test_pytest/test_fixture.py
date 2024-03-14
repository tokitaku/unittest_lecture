import pytest


@pytest.fixture
def setup():
    print('\n1. setup の前処理')
    # ここでテスト関数の前処理を行う

    yield  # ここでテスト関数を実行する

    print('4. setup の後処理')
    # ここでテスト関数の後処理を行う


def test_function1(setup):
    print('\n2. test_function1 内部の処理開始')
    assert 1 == 1
    print('3. test_function1 内部の処理終了')


def test_function2(setup):
    print('\n2. test_function2 内部の処理開始')
    assert 2 == 2
    print('3. test_function2 内部の処理終了')
