from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .utils.db_util import user_exists, add_user


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('retrodoro')

    return render(request, 'retrodoro/login_page.html')

def logout_page(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')

def registration_page(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'retrodoro/registration_page.html', context)

def retrodoro(request):
    return render(request, 'retrodoro/retrodoro.html')