from django.urls import path, include
from .views import *
from . import views

app_name = 'main'

urlpatterns = [
    path('', index),
    path('', include('cart.urls')),
    path('', include('authentication.urls')),
    


    path('home', homePage, name='home'),
    path('sale', salePage, name='sale'),
    path('clothes2', views.clothes_list, name='clothes_list'),
    path('accessories', views.accessories_list, name='accessories_list'),
    path('bags', views.bags_list, name="bags_list"),
    path('information', informationPage, name='information'),
   

    # PRODUCTS HTML - Страница с товарами
    # одежда
    path('platya', views.dresses_list, name="dresses_list"),
    path('zhakety', views.jackets_list, name="jackets_list"),
    # аксессуары
    path('ochki', views.glasses_list, name="glasses_list"),
    path('bizhuteriya', views.bijouterie_list, name="bijouterie_list"),



    path('basket22', basketPage, name='basket22'),
    # Отображение списка товаров 
    path('basket', views.product_list, name='product_list'),
    # Отображение товаров по категориям 
    path('<slug:category_slug>/', views.product_list, 
    name='product_list_by_category'), 

    # Отображение товаров по отдельности
    path('<int:id>/<slug:slug>', views.product_detail, 
    name='product_detail')

    
   
]

