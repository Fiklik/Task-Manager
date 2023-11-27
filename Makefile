runserver:
	poetry run python3 manage.py runserver

linter:
	poetry run flake8 .

black:
	poetry run black .

test:
	poetry run python3 manage.py test

test-report:
	poetry run coverage report

git message:
	make linter
	git add .
	git commit -m '$(message)'

push:
	git push