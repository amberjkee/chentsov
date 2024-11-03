from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('order<int:num>', views.order),
]
