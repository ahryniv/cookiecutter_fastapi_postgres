import logging
from http import HTTPStatus

from fastapi import Request, Response, FastAPI
from fastapi.responses import JSONResponse

from {{cookiecutter.project_slug}} import exceptions

logger = logging.getLogger(__name__)


def http_client_exception_handler(request: Request, exc: exceptions.HTTPClientException) -> Response:
    logger.error({
        'message': str(exc),
        'user_id': getattr(request.state, 'user_id', None),
    })
    return JSONResponse(
        status_code=HTTPStatus.BAD_GATEWAY,
        content=HTTPStatus.BAD_GATEWAY.phrase,
    )


def init_exception_handlers(app: FastAPI):
    app.exception_handler(exceptions.HTTPClientException)(http_client_exception_handler)
