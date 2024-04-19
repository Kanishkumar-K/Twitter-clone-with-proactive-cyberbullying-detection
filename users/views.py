from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout  # Import the logout function


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, f'Account has been updated.')
            return redirect('profile')
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'uform': uform, 'pform': pform})



@login_required
def SearchView(request):
    if request.method == 'POST':
        kerko = request.POST.get('search')
        print(kerko)
        results = User.objects.filter(username__contains=kerko)
        context = {
            'results':results
        }
        return render(request, 'users/search_result.html', context)

from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')  # Optional: Display a message
    return render(request, 'users/logout.html')

# views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import timedelta
from django.utils import timezone

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        # Retrieve username and password from form data
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a different page upon successful login
                return redirect('blog-home')
            else:
                # User account is inactive, redirect to inactive login page
                return render(request, 'inactive_login.html')
        else:
            # Authentication failed, display error message
            messages.error(request, 'Invalid username or password.')

    # If GET request or authentication failed, render login template
    return render(request, 'login.html')
