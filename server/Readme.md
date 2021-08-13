Запуск:

Установить докер 

```
sudo apt-get update && sudo apt-get install docker docker-compose
```

Билдим контейнер

```
docker build -t server .
```

Запустить контейнер c сервером

```
docker run -d server
```