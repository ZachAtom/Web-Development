# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm  # Correct import
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            username = form.cleaned_data.get('username')  # Get the username
            messages.success(request, f'Registration successful! Welcome to the site, {username}.')
            login(request, user)  # Log the user in
            return redirect('blog-home')  # Redirect to the home page
        else:
            print("Form is invalid. Errors:", form.errors)  # Debug statement
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})