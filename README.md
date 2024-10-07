# Connection between Postgres database and python (SQLAlchemy)

This project is an exemple of how you can deploy with Docker a PostGreSQL database and access it with python.

## Technologies

* `Docker` in order to dockerize our code. This make easier the deployment of our services

* `PostGreSQL` as database because it's largely used by firms

* `SqlAlchemy` for SQL querys

## PostGreSQL database

We deploy our PostGreSQL database. It can be visualize with some tools like DbVisualizer.

## USAGE

We run our services with this command :

`docker-compose build && docker-compose up db -d`

Wait for the database to be available and ready to accept connections...

Then :

`docker-compose up api` # need to add a healthcheck

## scripts annotation
* init.sql: initialize database
* docker-compose.yml: declare the Postgres database
    * declare the database as a service based on official postgres docker image

## Acknowledgement
This repo is cloned from https://github.com/Bessouat40/docker-postgres-sqlalchemy

The aim of this repository is to expand the learning and applications based on the tutorial.