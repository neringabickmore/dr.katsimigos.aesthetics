# [Aesthetics by Dr. Katsimigos](https://dr-katsimigos-aesthetics.herokuapp.com/)

This project is designed for an Aesthetics doctor who provides various beauty treatments. The project is designed to allow the owner of the site to manage all content (Add, Delete, Modify Content) by logging in. Site visitors can only view the content and has no rights to edit it.

## Terminal commands to run project locally

Activate virtual environment: ```.\.venv\Scripts\activate```

To run project locally: ```python manage.py runserver```

Update models:

```python
python3 manage.py makemigrations --dry-run
python3 manage.py makemigrations showmigrations
python3 manage.py migrate --plan             

python3 manage.py makemigrations
python3 manage.py migrate
