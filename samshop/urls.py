from . import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('login', auth_views.login, name='login'),
    path('admin', admin.site.urls),
]
