# Run Celery

celery -A address_microservice worker -l info -n worker1

celery -A employee_microservice worker -l info -n worker2

# Queue access

celery -A address_microservice amqp

celery -A employee_microservice amqp

# Queue Configure

## ZIP_CODE
queue.declare zip_code false true false false

exchange.declare topic_zip_codes topic false true false false

queue.bind zip_code topic_zip_codes zip_code

## Address

queue.declare address false true false false

exchange.declare topic_addresses topic false true false false

queue.bind address topic_addresses address