import gunicorn

import EmployeEmanagement
release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn  EmployeEmanagement.wsgi