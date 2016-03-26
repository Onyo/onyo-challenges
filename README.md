# Onyo Challenge #

Here we have some challenges for the following areas Backend, iOS and Android. Please feel free to enjoy our challenge and let us know if you have any question.

# Backend Challenge #

The main goal of this challenge is to exercise some concepts of API Rest, microservices and integrations. The basic goal is to create two APIs (microservices) using Django Rest Framework or similar web frameworks. These microservices should communicate with each other by JSONs, but should keep their databases separated. Both of them should answer to simple CRUD requests -- Get, Post, Put, Delete. We'll have two APIs, let's consider the first API "Ana" and the second one "Bob". When having a POST to Ana, Ana should perform a request to Bob and will save the answer of Bob on its own database. Bob should have API calls to return random values when its created, so when we have the same input coming from Ana we should have the same answer from Bob. In order to do it, Bob will have to store some data on its own database. The main reason is the needed decoupling between them.

The models, views and business rules may be created at your own criteria. We're interested on the dynamics that these parts will connect to each other.

As a topic we have a few suggestion:
- Bob could serve Postal Code Information (Street, City, State, etc) given a Postal Code it will return information. Ana should consume Bob and propagate its answer.


# TODO #

[ ] Fork challenge
[ ] creates django projects onyo-challenge
[ ] creates app postman
[ ] creates app secretary
[ ] create app postman on heroku
[ ] define DJANGO_MODULE_SETTINGS = postman
[ ] create app secretary on heroku
[ ] define DJANGO_MODULE_SETTINGS = secretary
[ ] deploy postman on heroku
[ ] deploy secretary on heroku
[ ] pull request


## App Postman
Postal Code Information microservice

[ ] creates model address 
[ ] creates test save address
[ ] creates postman view get
[ ] creates postman view post
[ ] creates postman view delete
[ ] creates postman view update
[ ] creates test view
[ ] loaddata postman


## App Secretary
Contacts microservice

[ ] creates model contact
[ ] creates test save contact
[ ] creates secretary view get
[ ] creates secretary view post
[ ] get address information on postman service
[ ] creates secretary view delete
[ ] creates secretary view update
[ ] creates test view

