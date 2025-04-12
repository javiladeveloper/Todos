from fastapi import FastAPI

from app.api.v1.routes import router as v1_router
from app.config import get_settings
from app.core.exceptions import ErrorLoggingMiddleware, add_exception_handlers
from app.core.logger import init_logging
from app.core.openapi import custom_openapi
from app.core.performance import PerformanceMiddleware
from app.graphql.schema import graphql_app
from app.infrastructure.repo_instance import repo_instance
from app.infrastructure.seeds import seed_data


def create_app() -> FastAPI:
    init_logging()
    settings = get_settings()

    seed_data(repo_instance)

    app = FastAPI(
        title=settings.api_title,
        version=settings.api_version,
        description=settings.api_description,
        contact={
            "name": settings.api_contact_name,
            "url": settings.api_contact_url,
            "email": settings.api_contact_email,
        },
        docs_url="/docs" if settings.env == "dev" else None,
        redoc_url=None,
    )

    add_exception_handlers(app)
    app.add_middleware(ErrorLoggingMiddleware)
    app.add_middleware(PerformanceMiddleware)
    api_version_prefix = f"/api/{settings.api_version_path}"
    app.include_router(v1_router, prefix=api_version_prefix)
    if settings.enable_graphql:
        app.mount("/", graphql_app)

    app.openapi = lambda: custom_openapi(app)
    return app


app = create_app()
