import fastapi
from mysite.api import user, category, product, subcategory, review, product_image, auth
import uvicorn
from mysite.admin.setup import setup_admin

store_app = fastapi.FastAPI()
store_app.include_router(user.user_router)
store_app.include_router(category.category_router)
store_app.include_router(product.product_router)
store_app.include_router(subcategory.subcategory_router)
store_app.include_router(review.review_router)
store_app.include_router(product_image.product_image_router)
store_app.include_router(auth.auth_router)
setup_admin(store_app)

if __name__ == '__main__':
    uvicorn.run(store_app, host="127.0.0.1", port=8000)