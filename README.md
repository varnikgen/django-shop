# django-shop

INSTALL
1. Install Postgres and create database
(on lixnux)
sudo apt install postgresql postgresql-contrib
sudo service postgresql start
sudo -u postgres psql postgres
CREATE DATABASE ecom_db;
CREATE USER ecomuser WITH PASSWORD 'devpass';
GRANT ALL PRIVILEGES ON DATABASE "ecom_db" TO ecomuser;
\q