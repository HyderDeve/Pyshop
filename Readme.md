# Pyshop

Small Django project (app: `products`) with a simple template layout and a Dockerfile for containerized development.

## Quick overview

- Django settings module: `pyshop.settings`
- Main app: `products/`
- Templates: `templates/` and `products/templates/`
- Dev server default port (project/Dockerfile): `3000`
- Entry point (local): `manage.py`

## Prerequisites

- Python 3.11 (project Dockerfile uses 3.11.4 by default)
- pip
- virtualenv (recommended)
- Docker (optional, for container builds)

Ensure a `requirements.txt` exists at the project root (the Dockerfile mounts and installs from it).

## Local development

1. Create and activate a virtual environment:
    ```
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # UNIX / macOS
    source .venv/bin/activate
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```
    python manage.py migrate
    ```

4. (Optional) Create a superuser:
    ```
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```
    python manage.py runserver 127.0.0.1:3000
    ```
    The app will be available at http://127.0.0.1:3000/

## Docker

Build and run the image. The Dockerfile expects `requirements.txt` in the project root.

1. Build:
    ```
    docker build -t pyshop:dev .
    ```
    Optionally override Python version:
    ```
    docker build --build-arg PYTHON_VERSION=3.11.4 -t pyshop:dev .
    ```

2. Run:
    ```
    docker run --rm -p 3000:3000 pyshop:dev
    ```

Notes:
- The Dockerfile creates a non-privileged user and exposes port `3000`.
- If you need persistent data or DB, mount volumes and configure environment variables accordingly.

## Project layout (relevant files)

- manage.py
- Dockerfile
- requirements.txt (expected)
- pyshop/
  - settings.py
  - urls.py
  - wsgi.py
- products/
  - models.py
  - views.py
  - urls.py
  - admin.py
  - templates/
     - index.html
- templates/
  - base.html
  - product_listing.html

## Useful management commands

- Run tests:
  ```
  python manage.py test
  ```
- Make migrations:
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
- Collect static files (if configured):
  ```
  python manage.py collectstatic
  ```

## .env example 
- SECRET_KEY = your_secret_key_from_settings.py

## Environment & security

- Do not hardcode SECRET_KEY or sensitive credentials in `settings.py`. Use environment variables or a secrets manager.
- Configure `ALLOWED_HOSTS` and `DEBUG` appropriately for production.
