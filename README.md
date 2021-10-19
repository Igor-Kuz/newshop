# E-commerce shop project based on Django framework. [![Build Status](https://app.travis-ci.com/Igor-Kuz/newshop.svg?branch=main)](https://app.travis-ci.com/Igor-Kuz/newshop)

### This project supports the following functions:
- registration of user
- authorization,
- adding goods to shop,
- adding images of goods
- search,


### For creating characteristics for goods in this project has been created separate app. 
### In this part of project user can:
- Create new category
- Create new characteristic(description) for goods
- Create value of characteristic 
- Create characteristic for goods
- Edit characteristics of goods
### So to create characteristics you need:
- Go to the admin area and create a product
- On the product page in the admin panel there will be a button "Create characteristics for the product"
- After that you will be taken to the characteristics admin page
- First, you need to create a characteristic and select the category to which it belongs.
- After that, you need to create a value for this characteristic.

Then, you can go to the next link - 'creating characteristics' for the product itself.

 
**Stack:**

 - Python >= 3.7

- Django >= 3

- django-crispy-forms==1.13.0

- Pillow==8.4.0

- bootstrap4

- sqlite3

### Инструменты разработки
##### 1) Открыть терминал или консоль и перейти в нужную Вам директорию

##### 2) Клонировать репозиторий и поставить звездочку)
    git clone git@github.com:Igor-Kuz/newshop.git

##### 3) Если Вы используете https, то: 
    git clone https://github.com/Igor-Kuz/newshop.git
    
    
##### 4) Создать виртуальное окружение
    python -m venv venv

##### 5) Активировать виртуальное окружение

    source venv/scripts/activate
##### или для Linux & MacOS
    source venv/bin/activate 
   
#### 6) Перейти в директорию newshop и  установить необходимые библиотеки командой
    pip install -r requirements.txt

##### 7) Выполнить миграции
    python manage.py makemigrations
    
    python manage.py migrate

##### 8) Создать суперпользователя
    python manage.py createsuperuser

##### 9) Запустить сервер
Запустить сервер - python manage.py runserver

#### После клонированя репозитория не забудьте создать директорию media, куда будут сохраняться изображения товара

#### Создание характеристик для товара

Зайти в админку и создайте товар
На странице товара в админке будет кнопка "Создать характеристики для товара"
После этого вы попадете на страницу админки характеристик
Сначала необходимо создать характеристику и выбрать категорию, к которой она относится
После этого необходимо создать для этой характеристики значение.
Затем, можно переходить к следующей ссылке - создание характеристики для самого товара.
