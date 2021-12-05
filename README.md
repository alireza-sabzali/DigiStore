# DigiStore
its a restfull api project 

# Install

docker volumes

```
  docker volume create postgres_data
  docker volume create app_static_volume
  docker volume create app_media_volume
```

docker network

```
  docker network create app_network
  docker network create nginx_network
```

docker command for installation
in the root of project.

```
  docker-compose up -d --build
  docker-compose exec web bash
```
  change directory to nginx/
  
```
  docker-compose up -d --build
```

# env files
you should create .env and .env.db files like this:

.env.db
POSTGRES_USER=hello_django
POSTGRES_PASSWORD=hello_django
POSTGRES_DB=hello_django_prod

.env
DEBUG=1
SECRET_KEY=django-insecure-cw2)7zm6%gf7(f_^3e6x0dr#3c-^omhx6yj-k5plwelys%1#iz
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_prod
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
