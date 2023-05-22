from fastapi import Depends, FastAPI

from app.routers import items, users, static

app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)
app.include_router(static.router)


@app.get("/")
async def root():
    return {"Hello": "World"}
