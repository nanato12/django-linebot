# django-linebot

DjangoでLINEBotを作りますよ〜

## 　環境

- Python 3.9.7
- Django 3.2.8

## パッケージ

- line-bot-sdk 1.20.0

## セットアップ

```sh
$ make run
```

## メモ

今後、また構築するときのために作業手順をメモしておく

1. docker環境の構築

2. webコンテナ内に入り、Djangoプロジェクトの作成

```plain
$ make exec
/code # django-admin startproject apps .
```

3. とりあえず、フォーマッタ、リンターをかける。

```plain
/code # make
manage.py:7: error: Function is missing a return type annotation
manage.py:7: note: Use "-> None" if function does not return a value
manage.py:22: error: Call to untyped function "main" in typed context
apps/settings.py:30: error: Need type annotation for "ALLOWED_HOSTS" (hint: "ALLOWED_HOSTS: List[<type>] = ...")
Found 3 errors in 2 files (checked 6 source files)
make: *** [Makefile:13: mypy] Error 1
```

自動生成されたファイルをリンターに沿って修正

## GitHub Actions

- **pychecker**

  python code check (black, flake8, isort, mypy)
  - [Repository](https://github.com/nanato12/pychecker)
  - [Marketplace](https://github.com/marketplace/actions/pychecker)
