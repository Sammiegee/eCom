from . import views
from django.urls import path
from django.contrib import admin

app_name = 'samshop'
urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('clothing', views.clothing, name='clothing'),
    path('footwear', views.footwear, name='footwear'),
    path('admin', admin.site.urls),
]
