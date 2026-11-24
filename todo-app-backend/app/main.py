from contextlib import asynccontextmanager

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends

from app.models.base import Base
from app.db.session import engine

from app.api.routes.task import router as task_router
from app.api.routes.category import router as category_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=task_router)
app.include_router(router=category_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

