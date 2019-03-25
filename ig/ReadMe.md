## Project name: Instagram

## Author: Alpha Mbabazi

## Description

This is an Instagram application that allows users to create their own account and add a biography and a profile picture to that account. the user will also be able to upload the picture and be able to view comments and likes on the posted or uploaded picture. 

## Set Up and Installations

* Ubuntu Software
* Python3.6
* Postgres
* python virtualenv

## Clone the Repo

Run the following command on the terminal: git clone https://github.com/AshleyAlpha/instag.git && cd gallery

## Activate virtual environment

* python3.6 -m venv --without-pip virtual,
* source virtual/bin/activate.
* then Activate virtual environment.       using python3.6 as default handler.

## Install dependancies

Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

## Database Creation
* psql
* CREATE DATABASE igram;

## .env file
Create .env file and paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = 'igram'
USER = ''
PASSWORD = ''
DEBUG = True

## How to run initial migration
* python3.6 manage.py makemigrations instag,
* python3.6 manage.py sqlmigrate (number of migration) instag then,
* python3.6 manage.py migrate.

## Technologies used
* Python 3.6
* HTML
* django-Bootstrap3
* Heroku
* Postgresql

## Support and contact details

 Contact me on mashleyalpha@gmail.com for any feedback

## License
MIT copyright (c) 2019 *Alpha Mbabazi*



