from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from user_authentication.models import UserProfile


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,  password=password)

        if user:
            login_django(request, user)
            return redirect('reports')
        else:
            return redirect(reverse('login'))


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        job = request.POST.get('job')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_exists = User.objects.filter(email=email).first()

        if user_exists:
            return HttpResponse('Já existe um usuário com este username')

        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        user_profile = UserProfile.objects.create(
            user=user, job=job)

        return redirect('login')


def logout(request):
    logout_django(request)
    return redirect(reverse('login'))
