from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "user/home.html")
def user_login(request):
    return HttpResponse ("login page")