# flask_heroku
Develop Flask app and deploy on the Heroku Cloud.

## Hello Flask app and Heroku

- [Chinese tutorial](https://mp.weixin.qq.com/s/ZJ2gLm59dOYJ7MybM5m6Yw)

### Prequisites
- Python
- pip
- Heroku CLI
- Git

### Install pipenv
To simplify the job, this tutorial uses pipenv.

install pipenv

```sh
pip3 install pipenv
```

### Create a simple Flask app

-  create a folder named autoflask(whatever you want) and 

```sh
# you need a unique app name for Heroku.
export APP=autoflask

# Create a folder named $APP(whatever you want) and jump in
mkdir $APP && cd $APP

# Create a virtual environment with pipenv and install Flask and Gunicorn 
pipenv install flask gunicorn

# Create a file named Procfile with the content.
echo 'web gunicorn wsgi:app' >Procfile

# Tell Heroku the Python verion you want.
echo 'python-3.8.6' >runtime.txt

# Create main.py in app folder and write the content.
mkdir app

cat > app/main.py <<EOF
from flask import Flask 
  
app = Flask(__name__) 
  
@app.route("/") 
def home_view(): 
        return "<h1>Welcome to Heroku</h1>"


EOF

# Create file wsgi.py and write the code.
cat >wsgi.py <<EOF
from app.main import app 
  
if __name__ == "__main__": 
        app.run() 
EOF

# Check if it works
pipenv run python3 wsgi.py
# Create your Heroku app(need login with Heroku CLI first.)
heroku create $APP

# deploy it on the Heroku Cloud 
git init
heroku git:remote -a $APP
git add .
git commit -m "hello flask"
git push heroku master

# Check your Heroku app.

```
Of course you can change autoflask to other unique app name and  run the above codes directly.

## Todo List

How Flask fits into MVC(Model-View-Controller) design pattern by building our 2nd Flask web application to display todo list.

- Install more packages

```sh
pipenv install psycopg2-binary flask-sqlalchemy
```
Noteice: install psycopg2-binary  only when you want to use Postgres

- MVC
  - Model: models.py
  - View: templates/index.html & static/main.css
  - Controller: routes.py 

- Database
  table(s):created automatically 
```
CREATE TABLE todo (
	id INTEGER NOT NULL, 
	text VARCHAR(200), 
	complete BOOLEAN, 
	PRIMARY KEY (id), 
	CHECK (complete IN (0, 1))
)
```
