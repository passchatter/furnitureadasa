from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'api'

urlpatterns = [
    path('signup/', views.Signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="api/login.html", authentication_form=LoginForm), name='login')
]