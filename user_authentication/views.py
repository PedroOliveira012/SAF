from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,  password=password)

        if user:
            login_django(request, user)
            return HttpResponse('autenticado')
        else:
            return HttpResponse(User.objects.filter(username=username).first())


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()

        if user:
            return HttpResponse('Já existe um usuário com este email')

        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()

        return HttpResponse('Usuario cadastrado com sucesso')
