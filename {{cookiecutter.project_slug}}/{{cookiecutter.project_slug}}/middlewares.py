import logging
from http import HTTPStatus

from fastapi import Request, Response, FastAPI
from starlette.middleware.cors import CORSMiddleware

from {{cookiecutter.project_slug}}.conf.settings import Settings

logger = logging.getLogger(__name__)


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as err:
        logger.exception({
            'message': str(err),
        })
        return Response(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, content=HTTPStatus.INTERNAL_SERVER_ERROR.phrase)


def init_middlewares(app: FastAPI, app_settings: Settings):
    app.middleware('http')(catch_exceptions_middleware)
    app.add_middleware(CORSMiddleware,
                       allow_origins=app_settings.ALLOWED_ORIGINS,
                       allow_credentials=True,
                       allow_methods=['*'],
                       allow_headers=["*"])
