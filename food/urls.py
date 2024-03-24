from django.urls import path
from . import views

urlpatterns = [
    path("products/",views.ProductListView.as_view()),
    path("category/",views.CategoryListView.as_view()),
    path("products/<int:id>/",views.ProductDetailCustom.as_view()),
    path("products/create/",views.api_product),
]