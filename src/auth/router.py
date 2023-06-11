from fastapi import APIRouter, Depends

from src.auth.security import get_current_user

router = APIRouter()


@router.get("/users/me", tags=['auth'])
async def akb_soc(username: str = Depends(get_current_user), ):
    return {"phone": username}
