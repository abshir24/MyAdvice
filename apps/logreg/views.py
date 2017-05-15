from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User


# Create your views here.

def login_page(request):
    return render(request,'logreg/login.html')

def register_page(request):
    return render(request,'logreg/registration.html')

def login(request):
    response_from_models = User.objects.login_user(request.POST)

    if response_from_models['status']:
        request.session['user_id'] = response_from_models['user'].id
        return redirect('main:home')
    else:
        messages.error(request, response_from_models['errors'])
        return redirect('logreg:login_page')


def register(request):
    response_from_models = User.objects.register_user(request.POST)

    if response_from_models['status']:
        request.session['user_id'] = response_from_models['user'].id
        return redirect('main:home')
    else:
        for error in response_from_models['errors']:
            messages.error(request, error)

        return redirect('logreg:index')

def logout(request):
    request.session.clear()
    return redirect('logreg:index')
