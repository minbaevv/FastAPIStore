from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session, selectinload
from typing import List

from mysite.database.models import Category
from mysite.database.schema import (
    CategoryInputSchema,
    CategoryOutSchema, CategoryUpdateSchema
)
from mysite.database.db import SessionLocal

category_router = APIRouter(prefix='/category', tags=['Category'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@category_router.post('/', response_model=CategoryOutSchema)
def create_category(
    category: CategoryInputSchema,
    db: Session = Depends(get_db)
):
    category_db = Category(**category.model_dump())
    db.add(category_db)
    db.commit()
    db.refresh(category_db)
    return category_db
@category_router.get('/', response_model=List[CategoryOutSchema])
def list_category(db: Session = Depends(get_db)):
    categories = (
        db.query(Category)
        .options(selectinload(Category.sub_categories))
        .all()
    )
    return categories
@category_router.get('/{category_id}/', response_model=CategoryOutSchema)
def detail_category(category_id: int, db: Session = Depends(get_db)):
    category = (
        db.query(Category)
        .options(selectinload(Category.sub_categories))
        .filter(Category.id == category_id).first())
    if not category:
        raise HTTPException(status_code=404, detail='Мындай категории жок')
    return category

@category_router.put('/{category_id}/', response_model=dict)
async def update_category(category_id: int, category: CategoryUpdateSchema,
                          db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()
    if not category_db:
        raise HTTPException(status_code=404, detail='Мындай id жок')

    for category_key, category_value in category.dict().items():
        setattr(category_db, category_key, category_value)
    db.commit()
    db.refresh(category_db)
    return {'message': 'Категории озгорулду'}

@category_router.delete('/{category_id}/', response_model=dict)
async def delete_category(category_id: int, db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()
    if not category_db:
        raise HTTPException(detail='Мындай категории жок', status_code=404)

    db.delete(category_db)
    db.commit()
    return{'message': 'Категории удалить болду'}