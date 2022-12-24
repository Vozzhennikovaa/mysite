from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/',views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),


    path('orders_buy', views.orders_buy_Page, name="orders_buy"),
     
    path('like', views.like_detail, name='like_detail'),
    path('addd/<int:product_id>/',views.like_add,name='like_add'),
    path('removee/<int:product_id>/',views.like_remove,name='like_remove'),

     
]

