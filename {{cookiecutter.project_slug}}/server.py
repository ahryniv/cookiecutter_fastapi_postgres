import uvicorn

from {{cookiecutter.project_slug}}.app import create_app
from {{cookiecutter.project_slug}}.conf.logging import LOG_CONFIG
from {{cookiecutter.project_slug}}.conf.settings import settings

app = create_app()


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=settings.API_PORT,
        log_level=settings.LOG_LEVEL.value.lower(),
        log_config=LOG_CONFIG,
        loop='uvloop'
    )
