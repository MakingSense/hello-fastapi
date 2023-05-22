from fastapi import FastAPI

from app.routers import static

app = FastAPI()


app.include_router(static.router)


@app.get("/")
async def root():
    return {"Hello": "World"}
