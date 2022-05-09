from . import views
from django.urls import path
from django.contrib import admin

app_name = 'samshop'
urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('clothing', views.clothing, name='clothing'),
    path('footwear', views.footwear, name='footwear'),
    path('admin', admin.site.urls),
    path('search', views.search, name='search'),
    path('signup', views.signup, name='signup'),
]
