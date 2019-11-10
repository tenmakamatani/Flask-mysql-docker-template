#! /bin/sh

cd `dirname $0`

docker-compose exec mysql mysql -uroot -proot -e 'drop database TKKODC_backend; create database TKKODC_backend; use TKKODC_backend;'
docker-compose exec flask python models/information.py