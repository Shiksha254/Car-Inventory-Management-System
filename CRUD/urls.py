from django.contrib import admin
from django.urls import path
from . import views
from CRUD.views import *


urlpatterns = [
    path('', views.home, name='home'), 
    path('create_car/', views.create_car, name='create_car'),
    path('car_list/', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('car_list/', views.car_list, name='car_list'),
    path('car/<int:pk>/update/', views.update_car, name='update_car'),
    path('car/<int:pk>/delete/', views.delete_car, name='delete_car'),
]