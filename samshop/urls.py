from . import views
from django.urls import path
from django.contrib import admin

app_name = 'samshop'
urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('clothing', views.clothing, name='clothing'),
    path('footwear', views.footwear, name='footwear'),
    path('jewellery', views.jewellery, name='jewellery'),
    path('watches', views.watches, name='watches'),
    path('bags', views.bags, name='bags'),
    path('admin', admin.site.urls),
    path('search', views.search, name='search'),
    path('signup', views.signup, name='signup'),
    path('add/<int:product_id>', views.basket_add, name='basket_add'),
    path('remove/<int:product_id>', views.basket_remove, name='basket_remove'),
    path('basket', views.basket_detail, name='basket_detail'),
]
