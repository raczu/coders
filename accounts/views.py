from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from accounts.forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signupView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('/accounts/signup/')
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'accounts/signup.html', args)

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    args = {'form': form}
    return render(request, 'accounts/login.html', args)

def logoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required(login_url="/accounts/login/")
def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/account.html', args)