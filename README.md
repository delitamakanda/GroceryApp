# Grocery App
[![Django CI](https://github.com/delitamakanda/GroceryApp/actions/workflows/django.yml/badge.svg?branch=main)](https://github.com/delitamakanda/GroceryApp/actions/workflows/django.yml)
Example grocery app in Django 3

## Installation

```bash
python3 -m venv grocery

source grocery/bin/activate

python manage.py makemigrations --dry-run --verbosity 3 # test new models
```

## Usage

```bash
python manage.py makemigrations
python manage.py migrate

celery worker --app=grocery_app --loglevel=info

flower -A grocery_app --port=5555 --broker=redis://localhost:6379/0
```

```python

```

## Tests
```bash
python3 -m pytest
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## api

- <https://grocery-fr.herokuapp.com/>
