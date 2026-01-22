from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from mysite.database.models import SubCategory
from mysite.database.schema import (
    SubCategoryCreateSchema,
    SubCategoryOutSchema, SubCategoryUpdateSchema
)
from mysite.database.db import SessionLocal

subcategory_router = APIRouter(prefix='/subcategories', tags=['SubCategory'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@subcategory_router.post('/', response_model=SubCategoryCreateSchema)
def create_subcategory(
    data: SubCategoryCreateSchema,
    db: Session = Depends(get_db)
):
    subcategory = SubCategory(**data.model_dump())
    db.add(subcategory)
    db.commit()
    db.refresh(subcategory)
    return subcategory

@subcategory_router.get('/', response_model=list[SubCategoryOutSchema])
def list_subcategories(db: Session = Depends(get_db)):
    return db.query(SubCategory).all()


@subcategory_router.put('/{subcategory_id}/', response_model=SubCategoryOutSchema)
def update_subcategory(
    subcategory_id: int,
    data: SubCategoryUpdateSchema,
    db: Session = Depends(get_db)
):
    subcategory = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
    if not subcategory:
        raise HTTPException(status_code=404, detail='Мындай id жок')

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(subcategory, key, value)

    db.commit()
    db.refresh(subcategory)
    return subcategory



@subcategory_router.delete('/{subcategory_id}/', response_model=dict)
def delete_subcategory(
    subcategory_id: int,
    db: Session = Depends(get_db)
):
    subcategory = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
    if not subcategory:
        raise HTTPException(status_code=404, detail='Мындай категория жок')

    db.delete(subcategory)
    db.commit()
    return {'message': 'Подкатегория удалить болду'}