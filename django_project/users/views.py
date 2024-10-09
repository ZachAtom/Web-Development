from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from .forms import UserRegisterForm
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created!  You are able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})

def custom_logout_view(request):
    logout(request)
    return redirect('login')
