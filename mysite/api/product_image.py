from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session, selectinload
from typing import List
from mysite.database.models import ProductImage
from mysite.database.schema import ProductImageSchema
from mysite.database.db import SessionLocal

product_image_router = APIRouter(prefix='/image', tags=['Image'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@product_image_router.post('/', response_model=ProductImageSchema)
def create_product_image(
    image_data: ProductImageSchema,
    db: Session = Depends(get_db)
):
    product_image = ProductImage(**image_data.dict())
    db.add(product_image)
    db.commit()
    db.refresh(product_image)
    return product_image
