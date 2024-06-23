from django.urls import path
from . import views

urlpatterns = [
    path('pet/', views.pet_info, name='pet_info'),
    path('welcome/', views.welcome, name='welcome'),
    path('', views.welcome),
]
