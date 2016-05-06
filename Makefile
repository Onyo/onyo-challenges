
.PHONY: default clean pip test run

define CHECK_SCRIPT
import sys
if sys.getdefaultencoding() != "utf-8":
	print "Configure python default encoding to UTF-8"
	sys.exit(1)
endef
export CHECK_SCRIPT

default:
	@awk -F\: '/^[a-z_]+:/ && !/default/ {printf "- %-20s %s\n", $$1, $$2}' Makefile

clean: # remove temporary files
	@find . -name \*.pyc -delete
	@find . -name \*.orig -delete
	@find . -name \*.bak -delete
	@find . -name __pycache__ -delete
	@find . -name coverage.xml -delete
	@find . -name test-report.xml -delete
	@find . -name .coverage -delete

pip: # install pip libraries
	@pip install -r requirements.txt

pip_local: # install pip local libraries
	@pip install -r requirements-local.txt

run_migrate: # run all migrations
	python manage.py migrate

run: # run local server
	python manage.py runserver 0.0.0.0:8000 $(filter-out $@,$(MAKECMDGOALS))

deploy_ana: # deploy ana in heroku
	git push origin master
	git push -u heroku --all

deploy_bob: # deploy bob in heroku
	git push origin master
	git push -u heroku-bob --all

deploy_all: # deploy all in heroku
	git push origin master
	git push -u heroku-bob --all
	git push -u heroku --all

heroku_config: # set DJANGO_SETTINGS_MODULE and DJANGO_DEFAULT_MODULE in the heroku
	heroku config:set -a flavio-onyo-ana DJANGO_SETTINGS_MODULE=ana.settings
	heroku config:set -a flavio-onyo-ana DJANGO_DEFAULT_MODULE=ana
	heroku config:set -a flavio-onyo-ana BOB_URL=http://flavio-onyo-bob.herokuapp.com/addresses
	heroku config:set -a flavio-onyo-bob DJANGO_SETTINGS_MODULE=bob.settings
	heroku config:set -a flavio-onyo-bob DJANGO_DEFAULT_MODULE=bob

heroku_import: # import addresses in the heroku
	heroku run -a flavio-onyo-bob python manage.py importaddresses addresses.csv
