from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('order<int:num>', views.order),
    path('new_order', views.new_order, name='new_order'),
    path('new_customer', views.new_customer, name='new_customer'),
]
