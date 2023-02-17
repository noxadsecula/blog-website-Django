from django.contrib import admin
from django.urls import path
from user.views import loginUser,logoutUser,registerUser

urlpatterns = [
    path("register/",registerUser, name="register"),
    path("login/",loginUser, name="login"),
    path("logout/",logoutUser,name="logout")
]