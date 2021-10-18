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

4. linebotのappを作成する

```plain
/code # mkdir apps/bot
/code # python manage.py startapp bot ./apps/bot
```

5. apps/bot/urls.py の作成

```plain
/code # touch apps/bot/urls.py
```

その後、ルートの `apps/urls.py` にも追加

6. app_nameを設定しないといけないんだって

`apps/bot/apps.py`

```python
class BotConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.bot"  # 変更

```

`apps/settings.py`

```python
INSTALLED_APPS = [
    ...
    "apps.bot",  # 追加
]
```

7. ALLOWED_HOSTSの設定

ngrokで起動したら怒られたから設定

ローカル環境なので、一旦全ホスト許可

```python
ALLOWED_HOSTS = ["*"]
```

## GitHub Actions

- **pychecker**

  python code check (black, flake8, isort, mypy)
  - [Repository](https://github.com/nanato12/pychecker)
  - [Marketplace](https://github.com/marketplace/actions/pychecker)
