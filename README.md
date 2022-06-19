# sales-backend
Backend repo containing the project related API endpoints


## Installation and Usage

Install Python3 (Exact Version : Python 3.9.0)

Install virtualenv

```bash
pip install virtualenv
```
or
```bash
pip3 install virtualenv
```
Create a project folder and cd into project folder

Clone the repository

Add env file with Django secret key : SECRET_KEY=secret_value

Create virtualenv
```bash
virtualenv "envname"
```

Activate virtualenv

In Windows : 
```bash
"envname"/Scripts/activate
```
In Linux : 
```bash
source "envname"/bin/activate
```

cd into sales folder 

Install project related dependencies

```bash
pip install -r requirements.txt
```

## Usage

```bash
python manage.py migrate
python manage.py runserver
```

Django project will be running on localhost:8000

