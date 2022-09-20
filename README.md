
# PNLF Project

CRUD movements control created in Python with the Django framework.

## Authors

- [@FranciscoRdz2001](https://www.github.com/FranciscoRdz2001)


## Installation

Install PNLF-project dependencies with:

```bash
  pip install -r requirements.txt
```
Set your DB connection settings in .env file, example:
```bash
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'service': 'my_service',
            'passfile': '.my_pgpass',
        },
    }
}
```
Make migrations:
```bash
  python manager.py makemigrations
  python manager.py migrate
```

## How run
First you need to start Tailwind with the following command:
```bash
  python manage.py tailwind start
```
Next, start the Django server:
```bash
  python manage.py runserver
```

## Screenshots

![Principal page](https://i.imgur.com/pdIxHgl.png)

![Principal page](https://i.imgur.com/byDJuCB.png)

