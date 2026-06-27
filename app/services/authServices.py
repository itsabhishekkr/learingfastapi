from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth_schemas import UserRegistration,UserLogin
from app.models.tables import User,Task
from app.models.dataConfig import declarative_base,get_db
from app.core.security import hash_password,verify_password
from app.core.tokenveryfy import create_access_token,decode_token
async def register(user: UserRegistration,db: Session):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return {
            "message": "Email already exists"
        }

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }


async def userLogin(user: UserLogin,db: Session):
    existing_user = (db.query(User).filter(User.email == user.email).first())

    if not existing_user:
        raise HTTPException(status_code=404,detail="Wrong email")

    if not verify_password(user.password,existing_user.password):
        raise HTTPException(status_code=401,detail="Wrong password")
    token = create_access_token({"user_id": existing_user.id,"name": existing_user.name,"email": existing_user.email})
    return {
        "access_token": token,
        "token_type": "bearer"
    }