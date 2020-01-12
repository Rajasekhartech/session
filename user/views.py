from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request, "user/home.html")
def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, "user/home.html", context)
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "auth/login.html", context)
    else:
        return render(request, "user/login.html", context)
    return render(request, "user/login.html")
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user_login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})