from urllib.request import Request

from fastapi import HTTPException, Depends, APIRouter
from mysite.database.models import UserProfile
from mysite.database.schema import UserProfileInputSchema,UserProfileOutSchema
from mysite.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List

user_router = APIRouter(prefix='/user', tags=['User'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_router.get('/', response_model=List[UserProfileOutSchema])
async def list_user(db: Session = Depends(get_db)):
    return db.query(UserProfile).all()


@user_router.get('/{user_id}/',response_model=UserProfileOutSchema)
async def detail_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserProfile).filter(UserProfile.id==user_id).first()
    if not user:
        raise HTTPException(detail='Мындай id жок', status_code=404)
    return user