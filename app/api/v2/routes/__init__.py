from fastapi import APIRouter

from app.api.v1.routes.system_routes import router as system_router
from app.api.v1.routes.task_routes import router as task_router

router = APIRouter()
router.include_router(task_router, prefix="/tasks")
router.include_router(system_router, prefix="/system")
