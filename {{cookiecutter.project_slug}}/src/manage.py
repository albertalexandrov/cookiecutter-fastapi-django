import os

from fastapi_django.management import typer


if __name__ == '__main__':
    os.environ.setdefault("FASTAPI_DJANGO_SETTINGS_MODULE", "settings")
    typer()
