# Установка

1. Установить питон
sudo apt update && sudo apt install python3 -y

2. Установить pip и venv 
sudo apt install python3-venv python3-pip -y

3. Создать и активировать виртуальную среду
python3 -m venv .venv
source .venv/bin/activate

4. Установить  mysql (Для бекенда mysql)
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config mysql-server

5. pip install -r requirements.txt

6. Создать пользователя, БД, дать права
mysql -u root -p --execute "create database django_db; create user 'django_admin'@'localhost' identified by 'django_pass'; grant all on django_db.* to 'django_admin'@'localhost';"

Экспортировать БД: mysqldump -u root -p django_db > django_db.sql

# Инициализация

1. Создать проект Django
django-admin startproject correspondence

2. Создать БД
python manage.py migrate

3. Создать админа
python manage.py createsuperuser

