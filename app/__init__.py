
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

import os
import psycopg2

app = Flask(__name__) 

# if you configure Heroku Postgres addon, and database url info is stored in system variable, DATABASE_URL 
if os.environ.get('DATABASE_URL')=='True':
    app.config['SQLALCHEMY_DATABASE_URI'] = f"{os.environ['DATABASE_URL']}?sslmode=require"
    # conn = psycopg2.connect(DATABASE_URL, sslmode='require')
else:
    # or use SQLite
    file_path = os.path.abspath(os.getcwd())+"/todo.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path 
  


db = SQLAlchemy(app) 
  
  
from app import routes 