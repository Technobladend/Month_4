from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from posts.models import Post
from user.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from user.models import Profile
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "user/register.html", context={"form": form})
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/register.html', context={"form": form})
        form.cleaned_data.pop("password_confirm")
        image = form.cleaned_data.pop("image")
        if User.objects.filter(username=form.cleaned_data['username']).exists():
            form.add_error(None, "Username already exists")
            return render(request, "user/register.html", context={"form": form})
        user = User.objects.create_user(**form.cleaned_data)

        Profile.objects.create(user=user, image=image)
        return redirect('main_page')
        

def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "user/login.html", context={"form": form})
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/login.html', context={"form": form})
        user = authenticate(**form.cleaned_data)
        if user is None:
            form.add_error(None, "Wrong Username or Password")
            return render(request, "user/login.html", context={"form": form})
        login(request, user)
        return redirect('main_page')
    

def logout_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            logout(request)
        return redirect('main_page')
        

@login_required(login_url='login')
def profile_view(request):
    posts = request.user.posts.all()
    return render(request, 'user/profile.html', context={'posts': posts})



