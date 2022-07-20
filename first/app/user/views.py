from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from app.user.forms import RegistrationForm, LoginForm
from django.contrib import auth
from django.http import HttpResponseRedirect

def create_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password_confirm']
            user = User(**form.cleaned_data)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
        return redirect('books')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'user/registration.html', context=context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('books')
            else:
                return HttpResponseRedirect("/account/invalid/")

    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'user/login.html', context=context)


def user_logout(request):
    auth.logout(request)
    return redirect('books')