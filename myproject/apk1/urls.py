from django.urls import path
from . import views

urlpatterns = [
    path('main.html', views.say_hello)
]