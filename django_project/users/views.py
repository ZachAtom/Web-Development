# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm  # Correct import
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            username = form.cleaned_data.get('username')  # Get the username
            messages.success(request, f'Your account has been created! You are now able to log in')
            login(request, user)  # Log the user in
            return redirect('login')  # Redirect to the home page
        else:
            print("Form is invalid. Errors:", form.errors)  # Debug statement
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required  # Ensures only logged-in users can access this view
def profile(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'users/profile.html', {'user': user})
