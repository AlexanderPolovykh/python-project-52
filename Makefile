postgres:
	sudo service postgresql start

run:
	python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

start: postgres
	python manage.py runserver
