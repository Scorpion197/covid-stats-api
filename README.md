# Covid-stats-api

An API for fetching latest corona virus stats.

# Setting up docker
Run the following commands to build the docker image
```
docker volume create --driver local --opt type=none --opt device=/var/lib/postgresql/data --opt o=bind dbdata
docker-compose build
docker-compose up
```
# Available endpoints

```
http://localhost:8000/api/allcountries
http://localhost:8000/api/getcountry/?country_name=COUNTRY_NAME
```
