# Desafio Onyo #

Requirements
============

* python >= 3.5.1
* virtualenvwrapper >= 3.5
* django >= 1.9.6

Make commands
=============

- clean                 # remove temporary files
- pip                   # install pip libraries
- pip_local             # install pip local libraries
- run_migrate           # run local all migrations
- run                   # run local server
- deploy_ana            # deploy ana in heroku
- deploy_bob            # deploy bob in heroku
- deploy_all            # deploy all in heroku
- heroku_config         # set DJANGO_SETTINGS_MODULE, DJANGO_DEFAULT_MODULE and BOB_URL in the heroku
- heroku_sqlmigrate     # run sqlmigrate in the heroku
- heroku_migrate        # run migrate in the heroku
- heroku_import         # import addresses in the heroku
- heroku_test_ana       # run unit tests ana
- heroku_test_bob       # run unit tests bob


Setup your local environment
============================

    mkvirtualenv onyo

Install the required python packages.

    make pip_local
    
Run local migrate.

    make run_migrate

Run server

    make run


Deploy heroku
============================

Create remote branches

    git branch add origin https://github.com/flaviohenriqu/onyo-challenges.git
    git branch add heroku https://git.heroku.com/flavio-onyo-ana.git
    git branch add heroku-bob https://git.heroku.com/flavio-onyo-bob.git
    
Push and deploy heroku

    make deploy_all
    
Set config environment in the heroku

    make heroku_config
    
Heroku run sqlmigrate

    make heroku_sqlmigrate

Heroku run sqlmigrate

    make heroku_migrate

Heroku run command 'importaddresses' to populate bob's addresses

    make heroku_import

Heroku run unit tests ana

    make heroku_test_ana

Heroku run unit tests bob

    make heroku_test_bob

# Usage #

## Bob

[Addresses Endpoint] (http://flavio-onyo-bob.herokuapp.com/addresses/)

    $ curl -X POST -H "Content-Type: application/json" http://flavio-onyo-bob.herokuapp.com/addresses/ -d '{"post_code": "54100200", "locality": "Av. Governador Agamenon Magalhães", "street_number": "2345", "country": "Brasil", "state": "Pernambuco", "city": "Recife"}'

## Ana

[Records Endpoint] (http://flavio-onyo-ana.herokuapp.com/records/)

    $ curl -X POST -H "Content-Type: application/json" http://flavio-onyo-ana.herokuapp.com/records/ -d '{"post_code": "49160210", "name": "Flavio Henrique", "email":"flavio@test.com"}' --verbose

# API Endpoints #

## Bob

About the API [http://flavio-onyo-bob.herokuapp.com/addresses/docs/] (http://flavio-onyo-bob.herokuapp.com/addresses/docs/)

## Ana

About the API [http://flavio-onyo-ana.herokuapp.com/records/docs/] (http://flavio-onyo-ana.herokuapp.com/records/docs/)


# Onyo Challenge #

Here we have some challenges for the following areas Backend, iOS and Android. Please feel free to enjoy our challenge and let us know if you have any question.

# Backend Challenge #

The main goal of this challenge is to exercise some concepts of API Rest, microservices and integrations. The basic goal is to create two APIs (microservices) using Django Rest Framework or similar web frameworks. These microservices should communicate with each other by JSONs, but should keep their databases separated. Both of them should answer to simple CRUD requests -- Get, Post, Put, Delete. We'll have two APIs, let's consider the first API "Ana" and the second one "Bob". When having a POST to Ana, Ana should perform a request to Bob and will save the answer of Bob on its own database. Bob should have API calls to return random values when its created, so when we have the same input coming from Ana we should have the same answer from Bob. In order to do it, Bob will have to store some data on its own database. The main reason is the needed decoupling between them.

The models, views and business rules may be created at your own criteria. We're interested on the dynamics that these parts will connect to each other.

As a topic we have a few suggestion:
- Bob could serve Postal Code Information (Street, City, State, etc) given a Postal Code it will return information. Ana should consume Bob and propagate its answer.
- Bob could be serving Lotto Check Service. Given 6 number, Bob will tell Ana if its a winner combination or not. Ana should cache its answer in order to avoid calling Bob many times.

Fell free to follow any topic, but please make sure you have understood the purpose of its challenge.

### **Must have** ###

* Unit tests
* Integrations tests
* Documentation
* Deployment (Heroku, Openshift, DigitalOcean)
* Clean, readable, maintainable, and extensible code 
* Decoupling on two different folders

### **Optional, but recommended** ###

* Django Rest Framework 
* Interface

### **ATENTION** ###
1. Don't worry about the topic you'll chose to work on. Fell free to work on a confortable topic.
2. You should not try to push changes directly to this repository.

### **Submission Process** ###
The candidate must implement the APIs and send a Pull Request to this repository with the solution.

The Pull request process works this way:

1. The candidate forks the repository (should not clone it directly)
2. Works on the code using the forked repository.
3. Commits and push changes to the forked repository.
4. Using the GitHub interface, send the pull request.

# iOS Challenge #

The iOS Challenge is available at: [ios-challenge.md](https://github.com/Onyo/onyo-challenges/blob/master/ios-challenge.md)

# Android Challenge #

The Android Challenge is available at: [android-challenge.md](https://github.com/Onyo/onyo-challenges/blob/master/android-challenge.md)
