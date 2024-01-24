from .views import *
from django.urls import path,include

urlpatterns = [
    path("",home,name = "home"),
    path("about",about,name = "about"),
]