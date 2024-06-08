from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns = [
    path('api/v1/products/', ProductList.as_view()),
    path('api/v1/products/<int:id>/',ProductDetail.as_view())
]