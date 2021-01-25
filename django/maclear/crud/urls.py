from django.urls import path, include
from crud import views as view

urlpatterns = [
    path('products', view.products),
    path('product/read/<int:id>', view.product_read),
    path('product/update/<int:id>', view.product_edit),
    path('product/delete/<int:id>', view.product_delete),
    path('product/add', view.product_add),
    path('product/images', view.product_images),
    path('product/image/delete/<int:id>', view.product_image_delete)
]