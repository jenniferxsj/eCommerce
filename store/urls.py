from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name = "store"),
    path('cart/', views.cart, name = "cart"),
    path('add_item/', views.addItem, name="add_item"),
    path('product/<int:id>', views.product_detail, name='product_detail'),
] 