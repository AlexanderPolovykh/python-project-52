postgres:
	echo "123" | sudo --stdin service postgresql start

run:
	python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

start: postgres
	python manage.py runserver

lint:
	poetry run flake8 .
