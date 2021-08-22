

from django.contrib import admin
from django.urls import path
from .views import index, login, signup, logout, cart,order, address, thankyou,review_order,\
    order_list,address_list,add_address
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
    path('cart', cart, name='cart'),
    path('address', address, name='address'),
    path('empty_cart', cart, name='cart'),
    path('empty_customer_cart', cart, name='cart'),
    path('review_order', review_order, name='review_order'),
    path('thankyou', thankyou, name='thankyou'),
    path('order', order, name='order'),
    path('order_list', order_list, name='order_list'),
    path('address_list', address_list, name='address_list'),
    path('add_address', add_address, name='add_address'),



    path('reset_password', auth_views.PasswordResetView.as_view(),
         name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/uidb64/<token>', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(
    ), name='password_reset_complete')

]
