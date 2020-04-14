**---PyCharm:---**  
File -> Settings -> Version Control -> Git -> Path  
File -> Settings -> Version Control -> Github -> login  
VCS -> Checkout from Version Control -> Git

**---Terminal:---**  
-Создание виртуального окружения:  
python -m venv espenv

**---PyCharm:---**  
-Запуск виртуального окружения:  
File -> Settings -> Project Settings -> Project Interpreter -> Add Local  (Scripts -> python.exe)

-Установка зависимостей:  
pip install -r requirements.txt

-Запуск сервера:  
python devmanage.py runserver
