#!/usr/bin/env bash

# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
# pip install -r requirements.txt
# poetry install

# Convert static asset files
# python manage.py collectstatic --no-input

# Postgres позволяет подключиться к удаленной базе указав ссылку на нее после флага -d
# ссылка подгрузится из переменной окружения, которую нам нужно будет указать на сервисе деплоя
# дальше мы загружаем в поключенную базу наш sql-файл с таблицами
DATABASE_URL=${DATABASE_URL:-postgresql://polovykh:123@localhost/task_manager}
make install && psql -a -d $DATABASE_URL -f database.sql

# Apply any outstanding database migrations
python manage.py migrate
