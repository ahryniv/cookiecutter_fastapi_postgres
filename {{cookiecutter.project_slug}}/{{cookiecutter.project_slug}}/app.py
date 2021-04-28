from {{cookiecutter.project_slug}}.database import CookieCutterSession, metadata
from fastapi import FastAPI
from sqlalchemy import create_engine

from {{cookiecutter.project_slug}} import __version__
from {{cookiecutter.project_slug}}.api import {{cookiecutter.project_slug}}_base
from {{cookiecutter.project_slug}}.conf.sentry import init_sentry
from {{cookiecutter.project_slug}}.conf.settings import settings, Env, Settings
from {{cookiecutter.project_slug}}.exception_handlers import init_exception_handlers
from {{cookiecutter.project_slug}}.middlewares import init_middlewares


def _init_db(app_settings: Settings):
    engine = create_engine(app_settings.sqlalchemy_database_uri)
    CookieCutterSession.configure(bind=engine)
    metadata.bind = engine


def create_app(app_settings: Settings = None):
    app_settings = app_settings if app_settings is not None else settings
    init_sentry(app_settings, version=__version__)
    is_production = app_settings.ENV == Env.PRODUCTION
    app = FastAPI(
        title='{{cookiecutter.project_name}}',
        description='{{cookiecutter.description}}',
        debug=app_settings.DEBUG,
        docs_url='/docs' if not is_production else None,
        redoc_url='/redoc' if not is_production else None,
        version=__version__,
    )
    init_middlewares(app, app_settings)
    init_exception_handlers(app)
    _init_db(app_settings)

    # routes
    app.include_router({{cookiecutter.project_slug}}_base.router, tags=['{{cookiecutter.project_name}}'])
    return app
