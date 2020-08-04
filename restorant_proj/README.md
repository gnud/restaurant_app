# Quick start

First we start by cloning the project's repo

```
git clone {TODO ADD URL}
```

now, cd into our project

```
virtualenv -p python3 venv
source venv/bin/activate
```

Note: we can replace venv with ~/.venvs/restorant_venv or
any full path to some venvs directory

# Install packages

```
pip install -r requirements.txt
```

Note: make sure virtualenv is loaded.

# Flake testing

Execute

```
flake8
```

In the project's root, where manage.py is located.

Expect output similar to:
```
./restaurant_proj/settings.py:90:80: E501 line too long (125 > 119 characters)
./restaraunt_api/tests.py:1:1: F401 'django.test.TestCase' imported but unused
./restaraunt_api/admin.py:1:1: F401 'django.contrib.admin' imported but unused
```

Note: make sure virtualenv is loaded.

# Usage

## Admin

An admin user I suppose the restaurant owner can login via the admin web interface, provide
via http://127.0.0.1/admin/

## Create a sample user

```bash
./manage.py createsuperuser --username='dominoes_cz' --email='owner@dominoes.cz'
# <type a password>
```

### Login

Login with sample user
and the owner can see Menus admin page.

The admin page for the menu has one field called company, which has also company admin, to be
able to use the popup in place for creating companies

## API

The browsable API located at
http://127.0.0.1:8000/api/v1/orders/ 


## Testing

First, make sure you are in root directory of the project.

Run

```bash
pytest
```

Sample output:
```bash
platform linux -- Python 3.6.9, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
django: settings: restaurant_proj.settings (from ini)
rootdir: .../restaurant_proj, configfile: pytest.ini
plugins: django-3.9.0, Faker-4.1.1
collected 1 item                                                                                                                                                                                                                                                        

restaraunt_api/tests/unit/test_orders.py .    
```

Or using Pycharm IDE:
- Check "Do not use Django test runner" in Settings/Frameworks/Django
- Settings/Tools/Python Integrated Tools in Testing group select default runner to be pytest
- Now either press the green play in one test_{x},py file, or create new Runner with Django Test

# Development

Release docker version

- Run flake8 to make sure all requirements are met
- Edit setting.py and bump the version variable
- Run ./bin/docker.build.sh to make a new image 
- TODO: for production you need to push the image to some private docker registry
- To test localy via docker compose: docker-compose up -d

## Other tricks

Reload static files if needed:

```bash
docker-compose exec djapp python manage.py collectstatic
```

Migrate migration files if new migration files

```bash
docker-compose exec djapp python manage.py migrate
```

# ENV file

1. Docker for now uses variables set in the environment in docker-compose.yml, but
can be extended to .env file
2. .env file for local development
