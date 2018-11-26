# Run Celery

celery -A address_microservice worker -l info

# Queue access

celery -A address_microservice amqp