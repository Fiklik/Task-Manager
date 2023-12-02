runserver:
	poetry run python3 manage.py runserver

start:
	poetry run gunicorn task_manager.wsgi:application

linter:
	poetry run flake8 .

black:
	poetry run black .

test:
	poetry run python3 manage.py test 

test-coverage:
	poetry run coverage run --source="task_manager" manage.py test task_manager

test-report:
	poetry run coverage report

git message:
	make linter
	git add .
	git commit -m '$(message)'

push:
	git push