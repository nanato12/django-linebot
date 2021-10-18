all: black flake8 isort mypy

black:
	black .

flake8:
	flake8 .

isort:
	isort .

mypy:
	mypy .

exec:
	docker exec -it web sh

run:
	docker-compose up --build

ngrok:
	ngrok http 8000 --region=ap
