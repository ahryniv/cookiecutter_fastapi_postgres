from fastapi import APIRouter, Request

from {{cookiecutter.project_slug}}.schemas.ok import OKSchema
from {{cookiecutter.project_slug}}.schemas.version import VersionSchema

router = APIRouter()


@router.get(
    '/health',
    summary='Health check',
    response_model=OKSchema,
)
async def health():
    """Shows status of the server"""
    return OKSchema()


@router.get(
    '/version',
    summary='Version',
    response_model=VersionSchema,
)
async def version(request: Request):
    """Shows application version"""
    return VersionSchema(version=request.app.version)
