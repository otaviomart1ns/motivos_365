from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', login_required(views.index), name='home')
]