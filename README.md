# newshop 
ecommerce shop project
educational project

Открыть терминал или консоль и перейти в нужную Вам директорию
Прописать команду git clone git@github.com:Igor-Kuz/newshop.git

Если Вы используете https, то: git clone https://github.com/Igor-Kuz/newshop.git
Прописать следующие команды:


python3 -m venv ДиректорияВиртуальногоОкружения
source ДиректорияВиртуальногоОкружения/scripts/activate  или source ДиректорияВиртуальногоОкружения/bin/activate для Linux & MacOS
Перейти в директорию 

Установить необходимые библиотеки
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate


Запустить сервер - python manage.py runserver

Важно создать директорию media, куда будут сохраняться изображения товара

Создание характеристик для товара

Зайти в админку и создайте товар
На странице этого же товара в админке будет кнопка "Создать характеристики для товара"
После этого вы попадете на страницу админки характеристик
Сначала необходимо создать характеристику и выбрать категорию, к которой она относится
После этого необходимо создать для этой характеристики значение
Как только все вышеперечисленное сделали, можно переходить к следующей ссылке - создание характеристики для самого товара.
