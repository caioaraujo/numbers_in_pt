start:
	python manage.py runserver

docker-build:
	docker build --tag=numbers_in_pt .
