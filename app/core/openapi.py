from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.config import get_settings
from app.docs.openapi_tags import openapi_tags_by_lang


def custom_openapi(app: FastAPI):
    settings = get_settings()
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=settings.api_title,
        version=settings.api_version,
        description=settings.api_description,
        routes=app.routes,
        contact={
            "name": settings.api_contact_name,
            "url": settings.api_contact_url,
            "email": settings.api_contact_email,
        },
    )

    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }

    lang = getattr(settings, "lang", "es")
    openapi_schema["tags"] = openapi_tags_by_lang.get(lang, openapi_tags_by_lang["es"])

    app.openapi_schema = openapi_schema
    return app.openapi_schema
