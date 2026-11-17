# KunUZ Django project

A Django-based news website.

## Requirements

- Python 3.11+
- pip

## Setup (Windows PowerShell)

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Open `.env` and replace `DJANGO_SECRET_KEY` with a newly generated secret key. Keep the real `.env` file private. Set `DJANGO_DEBUG=True` only for local development.

Generate a key with:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Run the project

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ and visit the admin panel at http://127.0.0.1:8000/admin/.

## Production

Set `DJANGO_DEBUG=False`, configure `DJANGO_ALLOWED_HOSTS` with your real hostnames, and provide `DJANGO_SECRET_KEY` through the hosting environment. Never commit a real secret key.
