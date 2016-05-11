# Onyo Challenges

This is the repository that contains the application made by Sérgio Berlotto to Onyo challenge.

This readme will explain all of this code.

Bob and Ana are both a RestAPI applications.

## Bob

The BOB api will search and return a complete address for the zip code informed in the url parameter as "number"

Enter:

* number

Return:

* state
* city
* street

## Ana

The ANA api is a Customer API. This receive name and zip code and add the state, city and street information on the customer record. To add this information, Ana call Bob Api to retrieve the data about zip code.

## Installation

Each api is a separated django project, and to install it run the following commands inside each bob/ana directory

    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py collectstatic --noinput
    $ python manage.py test # if you want to run the tests
    $ python manage.py runserver 0.0.0.0:[8|5]000

**Ports:** To Ana connect correctly in Bob api, run each api in a different port: 8000 and 5000 for example, if you run in the same machine. Configure the Bob url in Ana settings file in *BOB_API_URL* variable.


## Deploy

Ana and Bob APIs are running on Heroku server:

    http://ana-berlotto.herokuapp.com
    http://bob-berlotto.herokuapp.com

In the Bob API have many ZipCode for tests


## Why two applications ?

Simple, becouse in this way is more easy to scale the applications in separated environments, generating high disponibility and performance for both.
