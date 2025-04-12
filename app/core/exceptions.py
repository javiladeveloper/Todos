from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger import get_logger

logger = get_logger(__name__)


def add_exception_handlers(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        logger.warning(f"Validation error: {exc.errors()}")
        return JSONResponse(
            status_code=422,
            content={"detail": exc.errors()},
        )

    @app.exception_handler(TaskNotFoundError)
    async def task_not_found_handler(request: Request, exc: TaskNotFoundError):
        logger.warning(f"Task not found: {str(exc)}")
        return JSONResponse(
            status_code=404,
            content={"detail": str(exc)},
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        logger.error("Unhandled exception", exc_info=exc)
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"},
        )

    @app.exception_handler(PageOutOfRange)
    async def page_out_of_range_handler(request: Request, exc: PageOutOfRange):
        logger.warning(f"Página fuera de rango solicitada: {request.url}")
        return JSONResponse(status_code=422, content={"detail": "Page out of range"})

    @app.exception_handler(InvalidTaskData)
    async def invalid_task_data_handler(request: Request, exc: InvalidTaskData):
        logger.warning(f"Datos inválidos para tarea: {str(exc)}")
        return JSONResponse(status_code=422, content={"detail": str(exc)})


class ErrorLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as exc:
            logger.exception("Middleware captured unhandled error", exc_info=exc)
            return JSONResponse(
                status_code=500,
                content={"detail": "Unhandled internal error"},
            )


class TaskNotFoundError(Exception):
    """Raised when a task is not found in the repository."""

    pass


class PageOutOfRange(Exception):
    """Se lanza cuando la página solicitada excede el total disponible."""

    pass


class InvalidTaskData(Exception):
    """Se lanza cuando los datos de una tarea no cumplen las reglas de validación."""

    pass
