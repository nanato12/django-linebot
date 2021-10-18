FROM python:3.9-alpine

RUN apk update
RUN apk add gcc musl-dev make mysql nodejs npm

# npm packages
RUN npm install -g n
RUN npm install -g @vue/cli

# npm update
RUN npm install -g npm

# pip
RUN pip install --upgrade pip

# formatter, linter
RUN pip install black mypy isort flake8

# necessary packages
RUN pip install PyJWT pytz sqlparse

# django packages
RUN pip install django \
    django-cors-headers \
    django-filter \
    djangorestframework \
    djangorestframework-jwt
