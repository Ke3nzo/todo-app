from fastapi import APIRouter, Depends

from app.dependencies import get_category_service
from app.services.category import CategoryService
from app.schemas.category import CategorySchema, CategoryCreateSchema, CategoryUpdateSchema

router = APIRouter(prefix="/categories")


@router.get("")
def read_categories(
    category_service: CategoryService = Depends(get_category_service),
) -> list[CategorySchema]:
    return category_service.list_category()



@router.post("", status_code=201)
def create_category(
    payload: CategoryCreateSchema,
    category_service: CategoryService = Depends(get_category_service),
) -> CategorySchema:
    return category_service.create_category(category_create=payload)


@router.patch("/{category_id}")
def update_category(
    category_id: str,
    payload: CategoryUpdateSchema,
    category_service: CategoryService = Depends(get_category_service),
) -> CategorySchema:
    return category_service.update_category(category_id=category_id, category_update=payload)


@router.delete("/{category_id}", status_code=204)
def delete_category(
    category_id: str,
    category_service: CategoryService = Depends(get_category_service),
) -> None:
    category_service.delete_category(category_id=category_id)
