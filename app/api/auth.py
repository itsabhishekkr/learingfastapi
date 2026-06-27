# POST    /auth/register
# POST    /auth/login
# POST    /auth/logout
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth_schemas import UserRegistration,UserLogin
from app.services.authServices import register,userLogin
from app.models.dataConfig import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
async def register_user(user: UserRegistration,db: Session = Depends(get_db)):
    return await register(user, db)

@router.post("/login")
async def login_user(user: UserLogin,db: Session = Depends(get_db)):
    return await userLogin(user, db)

