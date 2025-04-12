import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.core.logger import get_logger

logger = get_logger(__name__)


class PerformanceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        logger.info(
            f"{request.method} {request.url.path} completado en {duration:.4f}s"
        )

        response.headers["X-Process-Time"] = str(duration)
        return response
