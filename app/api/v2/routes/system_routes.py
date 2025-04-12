from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/health", tags=["Sistema"], summary="Verifica el estado de la API")
def health_check():
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "message": "API is healthy",
        },
    )
