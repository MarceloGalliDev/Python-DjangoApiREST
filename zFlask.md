# Api-Flask-Model

## Install VirtualVenv
> python3 -m .venv venv
> .venv/Scripts/activate
> python.exe -m pip install --upgrade pip

## Install Flask
> pip install Flask

## Install SQLAlchemy
> pip install SQLAlchemy
> pip install Flask-SQLAlchemy

## Install mysqlclient
> pip install mysqlclient
> https://flask-mysql.readthedocs.io/en/stable/

## Install flask-migrate
> pip install flask-migrate

## Install marshmallow
> pip install flask-marshmallow

## Install flask-rest_framework
> pip install flask-restful

## Install marshmallow-SQLAlchemy
> pip install marshmallow-sqlalchemy

## Comandos FLASK
  - criar arquivo app.py
  - instanciar o servidor flask
  - set FLASK_APP=app no cmd
  - flask run
  - criar o models

  - flask db init
  - flask db migrate
  - flask db upgrade

  - $env:FLASK_ENV = "development"
  - $env:FLASK_APP = "app"
  - flask --app app run --debug

@ = %40

print(dir(app))