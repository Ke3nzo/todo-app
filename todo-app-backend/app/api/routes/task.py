from fastapi import APIRouter, Depends

from app.dependencies import get_task_service
from app.services.task import TaskService

from app.schemas.task import TaskSchema, TaskCreateSchema, TaskUpdateSchema

router = APIRouter(prefix="/tasks")


@router.get("")
def read_tasks(
    task_service: TaskService = Depends(get_task_service)
) -> list[TaskSchema]:
    return task_service.list_task()


@router.post("", status_code=201)
def create_task(
    payload: TaskCreateSchema,
    task_service: TaskService = Depends(get_task_service)
) -> TaskSchema:
    return task_service.create_task(task_create=payload)


@router.patch("/{task_id}")
def update_task(
    task_id: str,
    payload: TaskUpdateSchema,
    task_service: TaskService = Depends(get_task_service)
) -> TaskSchema:
    return task_service.update_task(task_update=payload, task_id=task_id)


@router.delete("/{task_id}", status_code=204)
def delete_task(
    task_id: str,
    task_service: TaskService = Depends(get_task_service)
) -> None:
    task_service.delete_task(task_id=task_id)
