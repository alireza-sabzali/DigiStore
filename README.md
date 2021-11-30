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
finished.
