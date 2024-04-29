
from django.urls import path
from . import views

urlpatterns = [

   
    path('', views.cart_summary, name="cart_summary"),

    path('checkout/', views.checkout, name="checkout"),
    path('order_summary/', views.order_summary, name="order_summary"),
   
    path('add/', views.cart_add, name="cart_add"),
    path('delete/', views.cart_delete, name="cart_delete"),
    path('update/', views.cart_update, name="cart_update"),




]
