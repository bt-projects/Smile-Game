# Smile-Game-
This is a smile web based game using Django.

![Homepage](/smile/assets/images/homepage.png)
![Signup](/smile/assets/images/register.png)
![Login](/smile/assets/images/login.png)
![Game](/smile/assets/images/after-login-homepage.png)

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

### How to create a test app and generatre password in Google
![Step1:](/smile/assets/images/kajg948rn5r09385.PNG)
![Step2:](/smile/assets/images/sajklf92384092.PNG)
![Step3:](/smile/assets/images/kjas9w38r90w.PNG)
 
### Google Developer Console for OAuth (3rd-party application)
[Google Developer Console](https://console.developers.google.com)
![Step 1:](/smile/assets/images/googleconsole.PNG)
![Step 2:](/smile/assets/images/googleconsole2.png)
![Step 3:](/smile/assets/images/google%20console%20file.PNG)

> Created by [Bishow Thapa](http://bishowthapa.com.np/) in Dec 20, 2022
