from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



def RegisterUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account Created successfully for {username}. You can login now')
            return redirect('login')

    else:
        form = CreateUserForm()
    context = {
        'form':form
    }
    return render(request, 'registration/register.html', context)



def LoginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect")
    return render(request, 'registration/login.html')


def LogoutUser(request):
    logout(request)
    return redirect('login')




# Create your views here.
