from fastapi import Depends, FastAPI

from app.dependencies import get_query_token
from app.internal import admin
from app.routers import items, users, static

app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)
app.include_router(static.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_query_token)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"Hello": "World"}
