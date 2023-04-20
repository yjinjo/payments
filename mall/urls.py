from django.urls import path
from mall import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("cart/<int:product_pk>/add/", views.add_to_cart, name="add_to_cart"),
]
