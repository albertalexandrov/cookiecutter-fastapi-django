from environs import Env

from fastapi_django.constants import EnvironmentEnum

env = Env()
env.read_env(".env", override=True)

ENVIRONMENT = EnvironmentEnum.get_environment()

API_PREFIX = env.str("API_PREFIX", default="/api")

{% if cookiecutter.integrate_prometheus|lower == "y" -%}
PROMETHEUS_ENABLED = env.bool("PROMETHEUS_ENABLED", default=True)
{%- endif %}

MANAGEMENT = [
    {
        "typer": "management:typer",
    }
]