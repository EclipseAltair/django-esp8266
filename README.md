**---PyCharm:---**  
File -> Settings -> Version Control -> Git -> Path  
File -> Settings -> Version Control -> Github -> login  
VCS -> Checkout from Version Control -> Git

**---Terminal:---**  
-Создание виртуального окружения:  
python3 -m venv espenv

**---PyCharm:---**  
-Запуск виртуального окружения:  
File -> Settings -> Project Settings -> Project Interpreter -> Add Local


-Установка зависимостей:  
pip install -r requirements.txt

-Запуск сервера:  
python3 manage.py runserver

-Запуск redis  
sudo service redis-server start

-Запуск celery  
celery -A django-esp8266 worker -B -l INFO
