from fastapi import HTTPException, status

TASK_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Task not found"
)
