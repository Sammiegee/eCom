from . import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('admin', admin.site.urls),
]
