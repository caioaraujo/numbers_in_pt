start:
	python manage.py runserver

docker-build:
	docker build --tag=numbers_in_pt .

docker-run:
	docker run -p 8000:80 numbers_in_pt

test:
	python manage.py test
