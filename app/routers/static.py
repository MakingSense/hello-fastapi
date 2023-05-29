from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("./static/favicon.ico")


@router.get("/robots.txt", include_in_schema=False)
async def robots():
    return FileResponse("./static/robots.txt")


@router.get("/version.txt", include_in_schema=False)
async def version():
    return FileResponse("./static/version.txt")
