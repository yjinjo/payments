from django.urls import path
from mall import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
]
