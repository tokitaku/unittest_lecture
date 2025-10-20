# Unit Test Lecture

Pythonのユニットテスト（pytest / unittest）を学習するためのプロジェクトです。

## 目次

- [環境構築](#環境構築)
- [仮想環境のアクティベート](#仮想環境のアクティベート)
- [パスについて理解する](#パスについて理解する)
- [テストの実行](#テストの実行)
- [プロジェクト構成](#プロジェクト構成)

---

## 環境構築

### 1. 仮想環境の作成

```bash
# 仮想環境を作成
python3 -m venv .venv
```

### 2. 仮想環境のアクティベート

```bash
# 仮想環境をアクティブ化
source .venv/bin/activate

# プロンプトが (.venv) に変わる
# (.venv) vscode ➜ /workspaces/unit_test $
```

### 3. 依存パッケージのインストール

```bash
# requirements.txt から一括インストール
pip install -r requirements.txt
```

### 4. 仮想環境の非アクティブ化

```bash
# 作業終了時
deactivate
```

---

## 仮想環境のアクティベート

### アクティベートとは？

仮想環境を「有効化」することで、プロジェクト専用のPython環境を使えるようにする操作です。

```bash
source .venv/bin/activate
```

### アクティベートすると何が起こる？

`.venv/bin/activate` スクリプトが以下の設定を自動で行います：

#### 1. PATH の設定（コマンド実行用）

```bash
# 仮想環境のbinディレクトリを PATH の先頭に追加
PATH="/workspaces/unit_test/.venv/bin:$PATH"
```

**効果**：
- `python` コマンドで仮想環境のPythonを使う
- `pip` で仮想環境にパッケージをインストール
- `pytest` コマンドが使える

#### 2. PYTHONPATH の設定（モジュールインポート用）

```bash
# プロジェクトルートを PYTHONPATH に追加
PYTHONPATH="/workspaces/unit_test:$PYTHONPATH"
```

**効果**：
- `from blackjack.card import Card` のようなインポートが可能
- テストファイルからプロジェクトのモジュールを参照できる

### 確認方法

```bash
# どのPythonを使っているか確認
which python
# → /workspaces/unit_test/.venv/bin/python

# PATH の確認
echo $PATH
# → /workspaces/unit_test/.venv/bin:...

# PYTHONPATH の確認
echo $PYTHONPATH
# → /workspaces/unit_test:

# Pythonのモジュール検索パスを確認
python -c "import sys; print('\n'.join(sys.path))"
```

---

## パスについて理解する

「パスを通す」とは、**コマンドやモジュールをどこからでも使えるようにすること**です。

### 1. PATH（実行可能ファイルのパス）

**用途**: シェルがコマンドを探す場所

```bash
# PATH の内容
echo $PATH
# /workspaces/unit_test/.venv/bin:/usr/local/bin:/usr/bin:/bin

# コマンド実行時の動作
python --version
# → シェルが PATH から python を探して実行
```

**PATH に含まれるもの**: 実行ファイル（python, pip, pytest など）

```bash
ls .venv/bin/
# python  python3  pip  pip3  pytest  activate  ...
```

### 2. PYTHONPATH（Pythonモジュールの検索パス）

**用途**: Pythonが `import` 文でモジュールを探す場所

```bash
# PYTHONPATH の内容
echo $PYTHONPATH
# /workspaces/unit_test

# インポート時の動作
python -c "from blackjack.card import Card"
# → Pythonが sys.path から blackjack モジュールを探す
```

**PYTHONPATH に含まれるもの**: Pythonパッケージ（blackjack, janken など）

```bash
ls /workspaces/unit_test/
# blackjack/  janken/  tests/  test_pytest/  ...
```

### PATH と PYTHONPATH の違い

| 項目 | PATH | PYTHONPATH |
|------|------|------------|
| **使用者** | シェル（bash等） | Pythonインタープリター |
| **用途** | コマンド実行 | モジュールインポート |
| **確認方法** | `echo $PATH` | `echo $PYTHONPATH` |
| **例** | `python`, `pytest` を探す | `blackjack`, `janken` を探す |

### パスが通っていないとどうなる？

#### PATH が通っていない場合

```bash
# エラー: コマンドが見つからない
python --version
# bash: python: command not found

# フルパス指定なら動く（面倒！）
/workspaces/unit_test/.venv/bin/python --version
```

#### PYTHONPATH が通っていない場合

```python
# エラー: モジュールが見つからない
from blackjack.card import Card
# ModuleNotFoundError: No module named 'blackjack'
```

---

## テストの実行

### pytest の実行

```bash
# 仮想環境をアクティブ化
source .venv/bin/activate

# すべてのテストを実行
pytest

# 特定のディレクトリのテストを実行
pytest tests/
pytest test_pytest/

# 特定のファイルを実行
pytest tests/test_card.py

# 詳細表示（-v オプション）
pytest tests/ -v

# 特定のテストメソッドを実行
pytest tests/test_card.py::test_card_score_ace
```

### unittest の実行

```bash
# 仮想環境をアクティブ化
source .venv/bin/activate

# ディレクトリ内のすべてのテストを実行
python -m unittest discover -s test_unittest -v

# 特定のファイルを実行
python -m unittest test_unittest.test_basic

# 特定のテストクラスを実行
python -m unittest test_unittest.test_player1.TestPlayer

# 特定のテストメソッドを実行
python -m unittest test_unittest.test_player1.TestPlayer.test_name
```

---

## プロジェクト構成

```
/workspaces/unit_test/
├── .venv/                      # 仮想環境（自動生成）
│   └── bin/
│       ├── activate            # アクティベートスクリプト
│       ├── python              # 仮想環境のPython
│       └── pytest              # pytestコマンド
├── blackjack/                  # ブラックジャックゲーム
│   ├── __init__.py
│   ├── card.py
│   ├── main.py
│   └── player.py
├── janken/                     # じゃんけんゲーム
│   ├── __init__.py
│   ├── hands.py
│   ├── main.py
│   └── referee.py
├── tests/                      # pytestテスト（ブラックジャック用）
│   ├── test_card.py
│   ├── test_judge_game.py
│   └── test_odds.py
├── test_pytest/                # pytest学習用テスト
│   ├── test_basic.py
│   ├── test_fixture.py
│   └── test_raises.py
├── test_unittest/              # unittest学習用テスト
│   ├── test_basic.py
│   ├── test_player1.py
│   └── test_referee1.py
├── working/                    # 練習用コード
│   ├── payroll.py
│   └── worker.py
├── requirements.txt            # 依存パッケージ一覧
├── pytest.ini                  # pytest設定ファイル
├── pyproject.toml              # プロジェクト設定
└── README.md                   # このファイル
```

---

## トラブルシューティング

### モジュールがインポートできない

```bash
# PYTHONPATH を確認
echo $PYTHONPATH

# 空の場合は、仮想環境を再アクティブ化
deactivate
source .venv/bin/activate

# または手動で設定
export PYTHONPATH=/workspaces/unit_test:$PYTHONPATH
```

### pytest が見つからない

```bash
# 仮想環境がアクティブか確認
echo $VIRTUAL_ENV
# → /workspaces/unit_test/.venv

# pytestがインストールされているか確認
pip list | grep pytest

# インストールされていなければ
pip install pytest
```

### Python のバージョン確認

```bash
# 仮想環境のPythonバージョン
python --version

# システムのPythonバージョン
/usr/bin/python3 --version

# どのPythonを使っているか確認
which python
```

---

## 参考リンク

- [pytest公式ドキュメント](https://docs.pytest.org/)
- [unittest公式ドキュメント](https://docs.python.org/ja/3/library/unittest.html)
- [Python仮想環境（venv）](https://docs.python.org/ja/3/library/venv.html)

---

## ライセンス

このプロジェクトは学習目的で作成されています。
