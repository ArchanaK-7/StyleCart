from django.shortcuts import render, redirect
from .models import Product

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login as auth_login, logout


def home(request):
    return render(request, 'home.html')


def products(request):

    products = Product.objects.all()

    return render(request, 'products.html', {'products': products})


def login_user(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            auth_login(request, user)

            return redirect('/')

    return render(request, 'login.html')


def register(request):

    if request.method == 'POST':

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/login')

    return render(request, 'register.html')


def cart(request):
    return render(request, 'cart.html')

def logout_user(request):

    logout(request)

    return redirect('/')    