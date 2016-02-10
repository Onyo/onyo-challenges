# Lotto Check Service (made for Onyo`s Admissional Challenge)

This is a Lotto Check Service made for Onyo`s Admissional Challenge and does not have any production application whatsoever. But it works, of course ;)

### Live demo

To see the live demos, use any of these links:

Ana: [http://lucianoratamero-onyo-ana.herokuapp.com/](http://lucianoratamero-onyo-ana.herokuapp.com/)

Bob: [http://lucianoratamero-onyo-bob.herokuapp.com/](http://lucianoratamero-onyo-bob.herokuapp.com/)

All: [http://lucianoratamero-onyo-all.herokuapp.com/](http://lucianoratamero-onyo-all.herokuapp.com/)

To access the admin interface, use the username **onyo** and the password **onyo-challenge**.

### How to use the APIs

Both Ana and Bob answer to POST requests in the following format:

```
{"numbers": [list-of-six-numbers-between-1-and-60]}
```

### Development setup

To setup this project to development, you need to clone this project, create and activate a virtualenv, install the dependencies and setup databases.

First, install some OS dependencies. This differs from distro to distro, so **I will only tell how to do it on Ubuntu 14.04**:

```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install python-dev libncurses-dev python-setuptools postgresql-9.5 postgresql-server-dev-9.5 git
```

After that, you need to install the virtualenv package through pip:

```
sudo easy_install pip
sudo pip install virtualenv
```

Then, we can install our project :)

```
git clone https://github.com/lucianoratamero/onyo-challenges.git
virtualenv onyo-challenges
cd onyo-challenges
source bin/activate
pip install -r requirements.txt
```

#### Databases setup

Before running migration to prepare your databases schema, you need to create ana_db and bob_db databases on postgres.

```
sudo -u postgres createdb ana_db
sudo -u postgres createdb bob_db
```

With the databases created, you need to configure the username and password to access postgresql databases. I usually use the role 'postgres', changing it's password to a random one.

```
sudo -u postgres psql
\password postgres
[the-password-you-want]
[the-password-you-want-again]
\q
```

Then, export the username and password as DB_USER and DB_PASS so our Django apps know how to connect to postgresql databases. I usually export both using the postactivate script, which is executed each time you activate this virtualenv. What you need to do is this:

```
export DB_USER=postgres && echo 'export DB_USER=postgres' >> bin/postactivate
export DB_PASS=[the-password-you-set-into-postgres] && echo 'export DB_PASS=[the-password-you-set-into-postgres]' >> bin/postactivate
```

Phew! Almost done! Now, all you need to do is to run the migration commands:

```
python manage.py migrate
python manage.py migrate --database=ana_db
python manage.py migrate --database=bob_db
```

If you have problems with postgresql peer authentication (as always ><), follow [these steps](http://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge) to fix it.

...aaaand that's it! To run the tests:

```
python manage.py test
```

To run you local server:

```
python manage.py runserver
```

### Deploying to heroku

To deploy this app to heroku, there's no need to be able to run the project locally - you just need to have cloned this project and have [heroku toolbelt installed](https://toolbelt.heroku.com/debian) =)

But before deploying, you need to [create and configure a new heroku app](https://devcenter.heroku.com/articles/git#creating-a-heroku-remote), so we can deploy to it. Remember your created heroku app name, it will be **very** important.

Then, you need to [set heroku configs accordingly](https://devcenter.heroku.com/articles/config-vars#setting-up-config-vars-for-a-deployed-application), so heroku knows which Django settings to use. The available options are 'config.heroku.ana.settings', 'config.heroku.bob.settings' and 'config.heroku.all.settings', to deploy Ana, Bob or All:

```
heroku config:set -a [heroku-app-name] DJANGO_SETTINGS_MODULE=[path.to.settings]
```

Then, push the changes to your heroku app:

```
git push heroku master
```

After pushing changes to heroku and with the app running, you need to setup your databases.

#### Heroku databases

If you are deploying **only Bob or Ana**, you need to setup that app's database specifically.

```
heroku run -a [heroku-app-name] python manage.py migrate --database=[django-app-name]_db
```

But if you're running **all**, you don't need to specify which database to use.

```
heroku run -a [heroku-app-name] python manage.py migrate
```

**Remember:** since Ana is **completely** decoupled from Bob but **depends** on it, if you are hosting Ana, you **need to configure** Bob's API URL on its environment - **even if it is running at the same host**:

```
heroku config:set -a [heroku-app-name] CURRENT_BOB_API_URL=[full-url-to-bob]
```

### Explaining some decisions

#### App structure

I decided on the approach of having only one Django project with decoupled apps to facilitate testing, make it easy to reuse code and have everything in only one codebase. The tradeoffs were the need of different settings for each kind of deployment and the need to have one big integration test that uses the [LiveServerTestCase](https://docs.djangoproject.com/en/1.9/topics/testing/tools/#django.test.LiveServerTestCase), which is usually used in acceptance/Selenium tests.

This app structure also decouples versions of API, and only needs the reconfiguration of core urls and settings to enable use of a new version of the API. The tradeoff is, well, the need to reconfigure core urls and settings to use a new version :P

#### Database structure

Well, managing databases is always nasty. In this case, since all databases needed to be decoupled (and heroku does **not** like **nor** enable multiple databases on free plans), the configurations for development and production were really different - and most of my time was wasted trying to get everything to work on heroku. But, really, deploying something like this to Amazon would be a breeze.

The thing is: heroku is not good to deploy real apps, bit is easy do configure and deploy simple apps. Since it was really easy to manage heroku applications using heroku toolbelt, I saw no need to make a fabfile for deployment. I know how to make one, but just thought that it wasn't necessary. Pragmatism, man, pragmatism.

#### Code decisions

My first idea was to make a full-fledged DDD app, with the domain layer completely decoupled from the view/serializer/model layers; and I tried. The tradeoff was the proliferation of files and confusion in recognizing each one's responsability, and I saw that everything became more confusing each time I attempted - so, instead, I decided to make it simple. The only design pattern I used, and barely, was the Repository, to Ana's API, because it needed to get info from Bob and I wanted to shield the view layer from the service layer. Beyond that, I saw no need to complicate things.

### That's all, folks!

Thanks for your time and for this challenge; it really brought me to think a lot of stuff I'm not used to. Too many months away from the back end makes you rusty. I hope that you enjoyed my code as much as I enjoyed making all this stuff up =)

See ya, guys! o/
