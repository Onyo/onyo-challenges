instructions:
	@echo ' run:   make install '
	@echo '  ==config queue== '
	@echo ' run  celery -A employee_microservice amqp'
	@echo ' run  queue.declare zip_code false true false false'
	@echo ' run  exchange.declare topic_zip_codes topic false true false false'
	@echo ' run  queue.bind zip_code topic_zip_codes zip_code'
	@echo ' run exit'
	@echo ' run  make run'
	@echo ' ==open new terminal== '
	@echo ' run  make celery'


install:
	@pip install -U -r requirements.txt
	@sudo docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 rabbitmq:3-alpine

run:
	@python manage.py makemigrations
	@python manage.py migrate
	@python manage.py runserver 8001

celery:
	@celery -A employee_microservice worker -l info -n worker2

test:
	@python manage.py test
