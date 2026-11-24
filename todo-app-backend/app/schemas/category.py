from pydantic import BaseModel, ConfigDict


class CategoryCreateSchema(BaseModel):
    name: str


class CategoryUpdateSchema(BaseModel):
    name: str | None = None


class CategorySchema(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(from_attributes=True)
