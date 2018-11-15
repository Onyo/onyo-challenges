.PHONY: upgrade-requirements
upgrade-requirements:
	@pipenv lock -r  > requirements.txt
	@echo '-r requirements.txt' > requirements-dev.txt
	@pipenv lock -r -d | grep -v '^-i ' >> requirements-dev.txt

.PHONY: run-attached-shell
run-attached-shell:
	@echo "------------------------------------------------------"
	@echo "To attach another shell on the same container execute:"
	@echo "\tdocker exec -it erp_erp_run_1 sh"
	@echo "To run the django service using:"
	@echo "\t./manage.py runserver 0.0.0.0:8000"
	@echo "------------------------------------------------------"
	@echo
	docker-compose up -d adminer
	docker-compose run --rm --service-ports erp sh

.PHONY: test
test:
	docker-compose -p erp-test build
	docker-compose -p erp-test run --rm erp ./manage.py test --no-input
