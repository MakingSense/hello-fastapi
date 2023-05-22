from fastapi import APIRouter, Depends

from app.dependencies import get_token_header

router = APIRouter()

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_users():
    # TODO: return an array of typed object
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me")
async def read_user_me():
    # TODO: return a typed object
    return {"username": "fake_current_user"}


@router.get("/{username}")
async def read_user(username: str):
    # TODO: return a typed object
    return {"username": username}
