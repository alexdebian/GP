##Привет!

##Это тестовое задание (фотогалерея).

###Для установки проекта локально требуется следующее:
* установите виртуальное окружение (virtualenv)
* выполните в консоли следующую команду для установки необходимых пакетов:
pip install -r requirements.txt
* скопируйте проект на локальный компьютер:
* для проекта выберите интерпретатор в настройках IDE (python 3.5)
* создайте базу данных (PostgreSQL), настройки указаны в файле settings.py
* создайте миграции при помощи команды: python manage.py makemigrations
* далее их необходимо применить: python manage.py migrate
* запустите сервер: python manage.py runserver


###Функционал проекта:
* регистрация
* аутентификация
* изменение данных пользователя
* восстановление пароля
* сброс пароля
* возможность заргузки файлов и картинок
* отображение загруженных картинок для авторизованного пользователя
* отображение загруженных картинок остальных пользователей