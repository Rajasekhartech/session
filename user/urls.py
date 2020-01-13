from django.urls import path
from .views import user_login, home ,user_register, user_logout
urlpatterns = [
    path('home',home, name = "home"),
    path('', user_login, name = "user_login"),
    path('register/', user_register, name = "user_register"),
    path('logout', user_logout, name ="user_logout"),
]