from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [

    path('Getpizzas', views.api_get_pizzas),
]
