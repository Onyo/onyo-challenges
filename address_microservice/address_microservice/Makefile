instructions:
	@echo ' run:   make install '
	@echo '  ==config queue== '
	@echo ' run  celery -A address_microservice amqp'
	@echo ' run  queue.declare address false true false false'
	@echo ' run  exchange.declare topic_addresses topic false true false false'
	@echo ' run  queue.bind address topic_addresses address'
	@echo ' run exit'
	@echo ' run  make run'
	@echo ' ==open new terminal== '
	@echo ' run  make celery'


install:
	@pip install -U -r requirements.txt

run:
	@python manage.py runserver

celery:
	@celery -A address_microservice worker -l info -n worker1

test:
	@python manage.py test
