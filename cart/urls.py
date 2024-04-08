from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.Cart, name='cart'),
    path('<int:pk>/', views.deletecart, name='deletecart'),
    path('addcart/', views.addcart, name='addcart'),
    path('order/', views.orderproduk, name='order'),
    path('getorder/', views.getorderproduk, name='getorder'),
    path('cartorder/', views.cartorder, name='cartorder'),
    path('allorder/', views.allorder, name='allorder')
]