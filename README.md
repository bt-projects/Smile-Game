# Smile-Game-
This is a smile web based game using Django.

## 1. Install all the requirement files in your computer by running:
- `pip install -r requirements.txt`

pip freeze outputs a list of all installed Python modules with their versions.
`pip freeze > requirements.txt`

## 2. Create a database name "smile" in xampp

## 3. Migrate table in your database

- `py manage.py makemigrations`
- `py manage.py migrate`

## 4. Start your project

- `py manage.py runserver`

Make sure to start your mysql in xampp before running your application

## 5. Additional
 - Create superuser in django dashboard: `py manage.py createsuperuser`
 - After creating superuser you can directly login with superuser username and password:
 - Superuser can delete and update all the users who have signup in the smile.
 
> Created by [Bishow Thapa](http://bishowthapa.com.np/) in Dec 20, 2022
