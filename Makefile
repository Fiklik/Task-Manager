runserver:
	poetry run python3 manage.py runserver

linter:
	poetry run flake8 .

git message:
	make linter
	git add .
	git commit -m '$(message)'

push:
	git push