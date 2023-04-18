from django.urls import path
from mall_test import views

urlpatterns = [
    path("payment/new/", views.payment_new, name="payment_new"),
    path("payment/<int:pk>/pay/", views.payment_pay, name="payment_pay"),
]
