from pydantic import BaseModel, EmailStr
from typing import Optional, List
from .models import StatusChoices
from datetime import date,datetime


class UserProfileInputSchema(BaseModel):
    first_name:str
    last_name:str
    username:str
    email:EmailStr
    password:str
    age: Optional[int]
    phone_number:Optional[str]


class UserLoginSchema(BaseModel):
    username:str
    password:str

class UserProfileOutSchema(BaseModel):
    id:int
    first_name:str
    last_name:str
    username:str
    email:EmailStr
    age: Optional[int]
    phone_number:Optional[str]
    status: StatusChoices
    date_registered: date

class CategoryInputSchema(BaseModel):
    category_image:str
    category_name:str





class CategoryOutSchema(BaseModel):
    id: int
    category_image: str
    category_name: str
    sub_categories: List['SubCategoryOutSchema']

    class Config:
        from_attributes = True


class SubCategoryCreateSchema(BaseModel):
    sub_category_name: str
    category_id: int

class SubCategoryUpdateSchema(BaseModel):
    sub_category_name: str
    category_id: int


class SubCategoryOutSchema(BaseModel):
    id: int
    sub_category_name: str
    category_id: int

    class Config:
        from_attributes = True

class CategoryUpdateSchema(BaseModel):
    category_image: Optional[str] = None
    category_name: Optional[str] = None

class ProductUpdateSchema(BaseModel):
    product_name:str
    price:int
    article_number:int
    description:str
    video:Optional[str]
    product_type:bool

class ProductInputSchema(BaseModel):
    subcategory_id:int
    product_name:str
    price:int
    article_number:int
    description:str
    video:Optional[str]
    product_type:bool

class ProductOutSchema(BaseModel):
    id:int
    subcategory_id:int
    product_name:str
    price:int
    article_number:int
    description:str
    video:Optional[str]
    product_type:bool
    created_date:datetime
    images: Optional[List['ProductImageSchema']] = []

    class Config:
        from_attributes = True

class ProductImageSchema(BaseModel):
    image:str
    product_id:int

    class Config:
        from_attributes = True

class ReviewSchema(BaseModel):
    id:int
    user_id:int
    product_id:int
    text:str
    stars:int
    created_date:date

class ReviewUpdateSchema(BaseModel):
    user_id:int
    product_id:int
    text:str
    stars:int

class ReviewCreateSchema(BaseModel):
    user_id:int
    product_id:int
    text:str
    stars:int