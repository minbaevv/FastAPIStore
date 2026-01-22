from .views import (
    UserProfileAdmin,
    TokenAdmin,
    CategoryAdmin,
    SubCategoryAdmin,
    ProductAdmin,
    ProductImageAdmin,
    ReviewAdmin
)
from fastapi import FastAPI
from sqladmin import Admin
from mysite.database.db import engine


def setup_admin(shop_app: FastAPI):
    admin = Admin(shop_app, engine)
    admin.add_view(UserProfileAdmin)
    admin.add_view(TokenAdmin)
    admin.add_view(CategoryAdmin)
    admin.add_view(SubCategoryAdmin)
    admin.add_view(ProductAdmin)
    admin.add_view(ProductImageAdmin)
    admin.add_view(ReviewAdmin)