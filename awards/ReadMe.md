## Project name: Awwards

## Author: Alpha Mbabazi

## Description

At Moringa school we create a lot of projects but we never know those projects rate with our peers. so this app will allow a user to post a project he/she created and get it reviewed by his/her peers. a user will also be able to rate other user's projects, search for posted projects, view projects overall score and view the profile pages of post's owner.

## Set Up and Installations

* Ubuntu Software
* Python3.6
* python virtual env
* django==1.11
* django-admin 
* Postgres(for DB)

## Clone the Repo

Run the following command on the terminal: git clone https://github.com/AshleyAlpha/award.git && cd awards

## Activate virtual environment

* python3.6 -m venv --without-pip virtual,
* source virtual/bin/activate.
* curl htttps://bootstrap.pypa.io/get-pip.py | python
* then Activate virtual environment.       using python3.6 as default handler.

## Install dependancies

Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

## Database Creation
* psql
* CREATE DATABASE;

## .env file
Create *.env* file and paste the following filling where appropriate:

* SECRET_KEY = '<Secret_key>'
* DBNAME = 'awwards'
* USER = ''
* PASSWORD = ''
* DEBUG = True

## How to run initial migration
* python3.6 manage.py makemigrations instag,
* python3.6 manage.py sqlmigrate (number of migration) instag then,
* python3.6 manage.py migrate.


## Support and contact details

 Contact me on mashleyalpha@gmail.com for any feedback

## License
MIT copyright (c) 2019 *Alpha Mbabazi*






