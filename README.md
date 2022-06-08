# [Aesthetics by Dr. Katsimigos](https://dr-katsimigos-aesthetics.herokuapp.com/)

### Terminal commands to run project locally

Activate virtual environment: ```.\.venv\Scripts\activate```

To run project locally: ```python manage.py runserver```

Update models:

```terminal
python3 manage.py makemigrations --dry-run
python3 manage.py makemigrations showmigrations
python3 manage.py migrate --plan             

python3 manage.py makemigrations
python3 manage.py migrate            
```