![docker-compose.production.yml](https://github.com/kom-ae/kittygram_final/actions/workflows/main.yml/badge.svg)

# Проект Kittygram
___
Проект нацелен на владельцев котов и кошечек, для публикации данных о своих питомцах. Зарегистрированные пользователи могут размещать информацию о своих любимцах. Пользователи могут указать кличку, цвет,  год рождения, достижения питомца и его фотографию.

### Стек используемых технологий
___
#### Backend:
1. Django
2. Django REST framework (DRF):

#### База данных:
SQLite или Postgres.

Для использования Postgres в качестве СУБД,  в файле .env, задайте значение переменной окружения `DBMS=postgres`.

#### Frontend:
SPA приложение.

React.

### Запуск проекта.
___
#### Локальный запуск.

Клонируйте репозиторий:

`git clone https://github.com/kom-ae/kittygram_final.git`

Перейдите в директорию `kittygram_final`:

`cd kittygram_final`

Запустите контейнеры командой:

`docker compose up -d`

Применение миграций и сбор статики выполняется автоматически.

Веб страница проекта будет доступна по адресу

http://127.0.0.1:9000

#### Запуск на удаленном сервере.
На удаленном сервере создайте директорию `kittygram`. В указанную директорию скопируйте подготовленный `.env` файл и `docker-compose.production.yml`.

Перейдите в директорию `kittygram`.

Запустите проект командой
`docker compose -f docker-compose.production.yml up -d`

Настройте nginx хоста на проброс запросов к проекту на порт 9000.


### Пример .env файла.
___

```
POSTGRES_DB=name_db  # Имя базы данных 
POSTGRES_USER=user_db  # Пользователь базы данных
POSTGRES_PASSWORD=password_user_db  # Пароль пользователя базы данных
DB_HOST=name_host_db  # Имя хоста с СУБД postgres
DB_PORT=5432  # Порт БД
SECRET_KEY=''  # секретный ключ для Django
DEBUG=True  # Режим дебага
ALLOWED_HOSTS=127.0.0.1,localhost  # список разрешенных хостов для подключения к Django
#Database Management System
DBMS=postgres  # СУБД 
```

___
Автор проекта: [Александр Комаров](https://github.com/kom-ae/)
