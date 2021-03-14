# FAPS -- Flask-Api-Project-Skeleton
A project kick starter for python flask framework

### Frameworks
* Flask
* Flask-RESTful
* Flask-SQLAlchemy
* Flask-JWT-Extended
* PyMySQL

### Installing
* set virtual env for python: `py -3 -m venv venv` (python 3 on windows)
* activate virtual environment: `venv\Scripts\activate`
* install dependencies: `pip install -r requirement.txt`

### Running for powershell (dev mode)
```shell
$env:FLASK_APP="server"
$env:FLASK_ENV="development"
flask run # start application
```

### Tree structure
```
┌─ server
│   ├── resources
│   │   ├── book.py
│   │   └── __init__.py
│   ├── models.py
│   ├── jwt
│   ├── bp
│   │   ├── auth.py
│   │   └── __init__.py
│   └── __init__.py
├── setup.py
├── requirements.txt
├── create_tables.py
├── README.md
└── MANIFEST.in
```