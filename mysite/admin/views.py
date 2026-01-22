from mysite.database.models import *
from sqladmin import ModelView


class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [
        UserProfile.id,
        UserProfile.first_name,
        UserProfile.last_name,
        UserProfile.username,
        UserProfile.email,
        UserProfile.age,
        UserProfile.phone_number,
        UserProfile.status,
        UserProfile.date_registered
    ]


class TokenAdmin(ModelView, model=Token):
    column_list = [
        Token.id,
        Token.user_id,
        Token.token,
        Token.created_date
    ]



class CategoryAdmin(ModelView, model=Category):
    column_list = [
        Category.id,
        Category.category_name,
        Category.category_image
    ]


class SubCategoryAdmin(ModelView, model=SubCategory):
    column_list = [
        SubCategory.id,
        SubCategory.sub_category_name,
        SubCategory.category_id
    ]


class ProductAdmin(ModelView, model=Product):
    column_list = [
        Product.id,
        Product.product_name,
        Product.subcategory_id,
        Product.price,
        Product.article_number,
        Product.product_type,
        Product.created_date
    ]



class ProductImageAdmin(ModelView, model=ProductImage):
    column_list = [
        ProductImage.id,
        ProductImage.image,
        ProductImage.product_id
    ]

class ReviewAdmin(ModelView, model=Review):
    column_list = [
        Review.id,
        Review.user_id,
        Review.product_id,
        Review.stars,
        Review.text,
        Review.created_date
    ]
