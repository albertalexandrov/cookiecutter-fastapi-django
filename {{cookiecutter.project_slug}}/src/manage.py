import os

from fastapi_django.management import cli
from fastapi_django.management.utils import register_command

{%- if cookiecutter.include_examples|lower == "y" %}
from commands.example_command import example_command

# регистрация кастомной команды
register_command(example_command)
{%- endif %}


if __name__ == '__main__':
    os.environ.setdefault("FASTAPI_DJANGO_SETTINGS_MODULE", "settings")
    cli()
