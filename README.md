# Weather

### Installation and setup
- ```sudo pip3 install -r requirements.txt```
- ```sudo -u postgres psql```
- ```create user weather_user;```
- ```create database weather_db owner weather_user;```
- ```\password weather_user;   (password for this user to db = mypassword)```
- ```python3 manage.py makemigrations```
- ```python3 manage.py migrate```
- ```python3 manage.py createsuperuser```

<br />

