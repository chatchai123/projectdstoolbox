
from django.urls import path,include

from app.views import *

urlpatterns = [
    path('',home, name='home'),
    path('create/',create,name='create'),
    path('managefood/<str:date>/',managefood,name='managefood_add'),
    path('select_date/',select_date,name='select_date'),
    path('history_sale/',select_date,name='select_date'),
    path('clear_food/',clearfood,name='clear_food'),
    path('updatefood/<int:id>/',updatefood,name='updatefood'),
    path('search/',search,name='search'),
    path('management/', admin1, name='management'),
    path('me/', Me, name='me'),
    path('signout', signout, name='signout'),
    path('registerXlogin', registerXlogin, name='registerXlogin'),
    path('register', register, name='register'),
    path('payment/', payment, name='payment'),
    path('user_management/', user_management_view, name='user_management'),
    path('upload_profile_image/', upload_profile_image, name='upload_profile_image'),path('add_product/', add_product, name='add_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('add_cart/<int:id>/', add_cart, name='add_cart'),
    path('cart/',cart,name='cart'),
    path('order',order,name='order'),
    path('preorder/', preorder, name='preorder'),
    path('orders/', order, name='admin_order_list'),
    path('orders/update/<int:order_id>/', order, name='update_order_status'),
    path('orders/view/<int:order_id>/', order, name='view_order'),
    path('orders/track/<int:order_id>/', order, name='track_order'),
    path('login', login, name='login'),
    path('managefood/', managefood, name='managefood'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('food/<int:id>/delete/', delete_food, name='delete_food'),
    path('admin1/', admin1, name='admin1'),
  
] 
