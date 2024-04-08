from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashindex'),
    path('addproduk/', views.addproduk, name='addproduk'),
    path('updateproduk/<int:pk>/', views.updateproduk, name='updateproduk'),
    path('delete/<int:pk>/', views.deleteproduk, name='deleteproduk')
]