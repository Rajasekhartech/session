from django.urls import path
from .views import user_login, home
urlpatterns = [
    path('',home, name = "home"),
    path('login', user_login, name = "login"),
]